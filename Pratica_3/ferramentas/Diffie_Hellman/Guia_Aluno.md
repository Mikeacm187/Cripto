# Consegues combinar um segredo debaixo de escuta?

FICHA PRÁTICA DE REDES · DIFFIE-HELLMAN

Nome: __________________________________ Turma: __________ Data: __________

Colega / grupo: __________________________________________________________

## O cenário

Tens dois PCs e uma ligação que pode ser observada. Alice e Bob precisam de combinar um segredo sem o enviar pela rede. Vais pôr o serviço a funcionar, investigar a captura e testar o que acontece quando alguém interfere.

Usa os programas fornecidos. Trabalha por desafios: prevê o resultado, executa, recolhe a prova e explica o que aconteceu. Não precisas de alterar código.

**Antes de começar:** abre um terminal na pasta alunos. Os comandos usam python3; no Windows usa py -3. Consulta Preparacao.html se precisares de preparar o posto.

**Em cada nova tentativa:** reinicia o servidor. Para interromper um programa, prime Ctrl+C.

**Percurso:** desafios 01-05, cerca de 90 minutos; desafio 06, mais 25 minutos. No desafio 05, resolve um cartão e usa os restantes como extensão.


## 01 / Põe o serviço online

Tens dois PCs. Alice tem de conseguir ligar ao serviço de Bob. Só podes avançar quando tiveres prova da ligação.

### Executa

1. Decide com o teu colega: quem fica com Alice e quem fica com Bob?
2. Descobre o IPv4 de cada PC: usa `ipconfig` no Windows, `ip addr` no Linux ou as definições de Rede no macOS.
3. No PC de Bob, abre um terminal na pasta alunos e executa:
```
python3 servidor.py --host 0.0.0.0 --segredo 7
```
4. No PC de Alice, abre o Wireshark. Seleciona a interface ligada à rede e inicia a captura com o filtro de captura `tcp port 5000`.
5. No terminal de Alice, executa o comando seguinte. Substitui 192.168.50.20 pelo IPv4 de Bob:
```
python3 cliente.py --host 192.168.50.20 --segredo 6
```
6. Para a captura. Guarda-a como 01_ligacao.pcapng. Aplica o filtro de visualização `tcp.port == 5000`.
7. Localiza o SYN, o SYN/ACK e o ACK que estabelecem a ligação.

### Recolhe a prova

IPv4 de Alice:

____________________________________________________________________

IPv4 de Bob:

____________________________________________________________________

Porta de origem de Alice:

____________________________________________________________________

Porta do serviço de Bob:

____________________________________________________________________

N.º dos pacotes SYN / SYN-ACK / ACK:

____________________________________________________________________

### Fecha o diagnóstico

Bob usa a porta 5000. Alice também tem de usar 5000 como porta de origem? Justifica com a captura.

____________________________________________________________________

____________________________________________________________________

## 02 / O que é que passou no fio?

A ligação funcionou. Agora tens de descobrir se o segredo foi enviado pela rede.

### Executa

1. Na captura anterior, clica num pacote da ligação com o botão direito. Seleciona Follow > TCP Stream.
2. Localiza a mensagem hello de Alice e a resposta de Bob.
3. Regista os valores de p, g, A e B que aparecem no fluxo.
4. Consulta os terminais. Regista o K calculado por Alice e o K calculado por Bob.
5. Procura no fluxo um campo que envie K. Não confundas um número que aparece no texto com um campo do protocolo.
6. Localiza a mensagem de texto e o campo mac.

### Recolhe a prova

p / g:

____________________________________________________________________

A enviado por Alice / B enviado por Bob:

____________________________________________________________________

K no terminal de Alice / K no terminal de Bob:

____________________________________________________________________

Campo que transmite K: encontrei / não encontrei:

____________________________________________________________________

Texto recebido por Bob:

____________________________________________________________________

### Fecha o diagnóstico

Conseguiste ler a mensagem no Wireshark? Então o acordo de um segredo tornou esta comunicação confidencial? Usa a captura para justificar.

____________________________________________________________________

____________________________________________________________________

## 03 / Explica o que os dois PCs fizeram

Os dois terminais mostram o mesmo K. Tens de explicar como chegaram lá sem enviar esse campo.

### Executa

1. Usa os valores públicos que recolheste: p = 23, g = 5, A e B.
2. Para esta sessão, Alice usou a = 6 e Bob usou b = 7.
3. Antes de calcular, prevê: os dois resultados seguintes vão coincidir?
4. Calcula com uma calculadora. O operador mod indica o resto da divisão inteira:
```
Alice: K = B^6 mod 23
Bob:   K = A^7 mod 23
```
5. Compara com os terminais. Liga os resultados aos passos da Aula 3: A = g^a mod p e B = g^b mod p.

### Recolhe a prova

Previsão antes do cálculo:

____________________________________________________________________

Cálculo de Alice:

____________________________________________________________________

Cálculo de Bob:

____________________________________________________________________

Valores públicos / valores que ficam em cada PC:

____________________________________________________________________

### Fecha o diagnóstico

Um colega afirma: «Se não vi K no fluxo, ninguém o consegue descobrir.» A captura é suficiente para provar isso? Escreve a tua hipótese antes do próximo desafio.

____________________________________________________________________

____________________________________________________________________

## 04 / Tenta descobrir o segredo

Tens a captura, mas não tens acesso aos segredos dos terminais. Será que os números escolhidos aguentam uma tentativa de descoberta?

### Executa

1. Usa apenas A e B da captura. Executa o comando seguinte, substituindo 8 e 17 pelos valores observados:
```
python3 observador.py --A 8 --B 17
```
2. Regista o resultado e compara-o com K da primeira sessão.
3. Reinicia Bob e Alice sem --segredo. Mantém os endereços corretos:

Bob:
```
python3 servidor.py --host 0.0.0.0
```
Alice - substitui o endereço pelo IPv4 de Bob:
```
python3 cliente.py --host 192.168.50.20
```
4. Captura a nova sessão e guarda-a como 04_nova_sessao.pcapng. Compara A, B e K com a sessão anterior.

### Recolhe a prova

Expoente compatível encontrado pelo observador:

____________________________________________________________________

K recuperado / K da primeira sessão:

____________________________________________________________________

A / B / K na nova sessão:

____________________________________________________________________

### Fecha o diagnóstico

O programa descobriu K usando dados públicos. O que tornou isso fácil neste exemplo? Escolher novos segredos resolve o problema de usar p = 23?

____________________________________________________________________

____________________________________________________________________

## 05 / A ligação avariou. Prova onde.

Escolhe um incidente. Antes de executar, escreve o que prevês observar. O teu diagnóstico tem de incluir evidência do terminal e da captura.

### Executa

1. Escolhe um dos cartões abaixo. Na extensão, resolve os restantes.
2. Inicia uma captura com o filtro `tcp port 5000 or tcp port 5001`.
3. Executa apenas o incidente escolhido. Regista o primeiro erro nos dois terminais.
4. Decide: o TCP chegou a estabelecer-se ou a falha aconteceu antes?
5. Corrige a causa. Reinicia os programas e prova que o serviço voltou a funcionar.
6. Guarda a captura como 05_incidente_A.pcapng, trocando A pela letra do teu cartão.

### Cartão A / Ninguém atende
No mesmo PC, termina Bob e executa `python3 cliente.py`. Depois repõe o serviço e repete.

### Cartão B / A porta mudou
No mesmo PC, inicia `python3 servidor.py`. Executa `python3 cliente.py --porta 5001`. Corrige o destino e repete.

### Cartão C / Funciona aqui, falha no outro PC
Em dois PCs, inicia Bob com `python3 servidor.py --segredo 7`. Alice tenta ligar ao IPv4 de Bob com o comando do desafio 01. Depois altera a escuta de Bob e repete.

### Cartão D / TCP abriu, mas a resposta não chega
No mesmo PC, inicia `python3 servidor.py --atraso 15 --segredo 7` e depois `python3 cliente.py --segredo 6`. Alice espera até 12 segundos por uma resposta. Retira o atraso, reinicia ambos e repete.

### Cartão E / Há rede, mas não há acordo
No mesmo PC, inicia `python3 servidor.py` e depois `python3 cliente.py --p 29`. Consulta os dois terminais. Corrige o parâmetro e repete.

Nos cartões realizados no mesmo PC, captura na interface loopback. No cartão C, captura na interface de rede de uma das pontas.

### Recolhe a prova

Cartão / previsão:

____________________________________________________________________

Sintoma e primeiro erro apresentado:

____________________________________________________________________

TCP estabelecido? Evidência e n.º de pacote:

____________________________________________________________________

Causa que identificaste:

____________________________________________________________________

Correção aplicada e prova de recuperação:

____________________________________________________________________

### Fecha o diagnóstico

Um colega diz: «É da rede.» Que evidência recolheste para localizar a falha com maior precisão?

____________________________________________________________________

____________________________________________________________________

## 06 / Alguém ficou pelo meio

Alice e Bob vão repetir a troca. Desta vez, Alice liga a Mallory e Mallory liga a Bob. Prevê se Bob vai detetar a alteração da mensagem.

### Executa

1. Usa o mesmo computador e abre três terminais na pasta alunos.
2. Inicia uma captura na interface loopback com o filtro `tcp port 5000 or tcp port 6000`.
3. No terminal 1, inicia Bob:
```
python3 servidor.py --segredo 7
```
4. No terminal 2, inicia Mallory:
```
python3 mitm.py --alterar
```
5. No terminal 3, executa Alice:
```
python3 cliente.py --porta 6000 --segredo 6
```
6. Regista a mensagem enviada por Alice e a mensagem aceite por Bob.
7. Regista os segredos apresentados nos três terminais.
8. Para a captura e guarda-a como 06_intermediario.pcapng. Aplica o filtro `tcp.port == 5000 || tcp.port == 6000`.
9. Analisa as duas ligações com Follow > TCP Stream. Retira o filtro de uma stream antes de procurar a outra.
10. Compara A enviado por Alice com A recebido por Bob. Faz o mesmo para B.
11. Se houver tempo, reinicia os três programas e repete sem --alterar. Compara os textos.

### Recolhe a prova

Previsão: Bob deteta / aceita a alteração? Porquê?:

____________________________________________________________________

Texto enviado por Alice:

____________________________________________________________________

Texto recebido por Bob / resultado do MAC:

____________________________________________________________________

K de Alice / K de Bob:

____________________________________________________________________

K de Mallory com Alice / K de Mallory com Bob:

____________________________________________________________________

A enviado / A recebido; B enviado / B recebido:

____________________________________________________________________

N.º de ligações TCP e respetivas portas:

____________________________________________________________________

### Fecha o diagnóstico

Bob aceitou um MAC válido. Isso prova que falou diretamente com Alice? Explica como Mallory conseguiu alterar a mensagem e propõe uma forma de autenticar a troca.

____________________________________________________________________

____________________________________________________________________

## Entrega o teu relatório de rede

1. Entrega esta ficha com as respostas dos desafios realizados.
2. Junta as capturas 01_ligacao.pcapng, 04_nova_sessao.pcapng e a captura do incidente escolhido.
3. Se realizaste o desafio 06, junta 06_intermediario.pcapng.
4. Assinala os números dos pacotes usados como prova. Não entregues apenas imagens de terminais sem explicação.

### Última decisão

Vais usar este programa para proteger uma conversa real? Justifica com dois resultados da experiência.

____________________________________________________________________

____________________________________________________________________

**Limite deste laboratório:** os números são pequenos de propósito. O programa envia texto em claro com HMAC, sem cifragem. Não autentica a identidade dos participantes. O objetivo é observar estas propriedades e os seus limites na rede.
