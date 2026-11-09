# Operação Rede em Risco — missão dos analistas

**Pergunta central:** em que pontos se consegue ler, alterar ou obter informação que devia estar protegida?

Segue a preparação em `COMECA_AQUI.md`. Os comandos partem sempre da pasta `alunos`. Em Windows, troca `.venv/bin/python` por `.venv\Scripts\python.exe`.

Em cada desafio: **prevê → executa → recolhe a prova → conclui**. Não alteres código. Nos resultados automáticos, escolhe os dados que respondem à pergunta: não copies toda a saída.

## 1. O chat antigo protege a conversa?

**Prevê:** se a captura não mostrar palavras legíveis, isso basta para afirmar que a conversa está segura?

Abre três terminais na pasta `alunos`. No primeiro, inicia o servidor:

```text
.venv/bin/python ferramentas/TP1/comunicacao/chat.py servidor
```

No segundo e no terceiro:

```text
.venv/bin/python ferramentas/TP1/comunicacao/chat.py cliente 127.0.0.1
```

Escolhe nomes diferentes. Captura na interface loopback com `tcp port 5001`. Espera que ambos estejam ligados. Um cliente envia `REUNIAO NA SALA DE REDES`; o outro responde `RECEBIDO`. Guarda `01_chat.pcapng`.

No Wireshark, identifica o texto que passou no fio. Compara-o com o texto apresentado na receção e com a linha «CIFRAÇÃO» no emissor. Regista os IP e as portas de uma ligação.

Depois executa:

```text
.venv/bin/python ferramentas/Pratica_1/challenge-01/caesar_breaker.py
.venv/bin/python ferramentas/TP1/cifra_substituicao.py
.venv/bin/python ferramentas/TP1/vigenere_demo.py
```

O primeiro apresenta candidatos de César; identifica o que faz sentido e a chave. O segundo usa o mapa já fornecido no TP1 para apresentar uma tentativa de decifração de um texto de substituição; não é um ataque automático ao chat. No terceiro, escolhe decifrar, introduz a chave `REDE` e a mensagem `IIGIJ`. Volta a cifrar o resultado com a mesma chave para confirmar.

**Prova:** um excerto do chat na captura, a sua mensagem original, a chave César e o resultado Vigenère.

**Conclui:** distingue César, substituição fixa e Vigenère. No chat, todos os clientes recebem a mesma proteção? Como seria afetada a segurança se um participante divulgasse o mapa? Um resultado legível obtido com uma chave conhecida demonstra que a cifra foi quebrada sem chave?

Fecha os clientes com `/sair` e o servidor com Ctrl+C.

## 2. «Passámos para AES. Está resolvido?»

A empresa propõe substituir a cifra antiga por AES. Antes de aprovar, testa o comportamento dos modos.

**Prevê:** quatro blocos iguais darão quatro blocos cifrados iguais em qualquer modo?

```text
.venv/bin/python ferramentas/Pratica_1/challenge-03/block_ciphers.py "Olá!"
.venv/bin/python ferramentas/Pratica_1/challenge-03/block_ciphers.py "AAAAAAAAAAAAAAAA"
.venv/bin/python ferramentas/Pratica_1/challenge-04/aes_modes.py
.venv/bin/python ferramentas/Pratica_1/challenge-05/modes_comparison.py
```

Regista o número de caracteres e bytes de `Olá!` e o padding dos dois exemplos. Compara os blocos repetidos em ECB/CBC, a alteração do IV e os blocos afetados pela alteração de um bit nos quatro modos. CFB nesta experiência usa feedback de 128 bits. Os índices de bytes começam em 0; os blocos são numerados a partir de 1.

**Prova:** um resultado de padding, um exemplo de repetição em ECB e a comparação dos blocos afetados pela adulteração.

**Conclui:** qual é a diferença entre ocultar o conteúdo e detetar alterações? Se a decifragem não produzir erro, podes concluir que ninguém alterou a mensagem? DES seria uma alternativa adequada a AES? Distingue tamanho do bloco de tamanho da chave.

**Se acabares cedo:**

```text
.venv/bin/python ferramentas/Pratica_1/challenge-04/bonus_bmp.py
```

Abre as imagens em `ferramentas/Pratica_1/evidence/bmp/` e escolhe uma comparação que ajude a explicar ECB.

## 3. Combinar um segredo numa rede observada

Agora a equipa tem outro problema: como combinar um segredo sem o enviar diretamente?

**Prevê:** quais dos valores públicos e privados esperas encontrar na captura?

Num terminal, inicia Bob:

```text
.venv/bin/python ferramentas/Diffie_Hellman/servidor.py --porta 5050 --segredo 7
```

Inicia uma captura loopback com `tcp port 5050 or tcp port 6060`. Noutro terminal, inicia Alice:

```text
.venv/bin/python ferramentas/Diffie_Hellman/cliente.py --porta 5050 --segredo 6 --mensagem "Autorizar envio do relatorio"
```

Guarda `03_dh_direto.pcapng`. Identifica SYN, SYN/ACK e ACK, os valores `p`, `g`, `A`, `B`, o campo `texto` e o MAC. Compara o segredo mostrado nos terminais com o conteúdo da captura.

Executa o observador com os valores A e B que recolheste. Com os segredos indicados, o comando será:

```text
.venv/bin/python ferramentas/Diffie_Hellman/observador.py --A 8 --B 17
```

**Incidente rápido:** reinicia Bob. Executa Alice com `--porta 5051` em vez de `5050`. Regista o erro e corrige o destino. Não confundas o erro de ligação com uma falha da matemática de DH.

### Um terceiro entra na conversa

Abre três terminais. Confirma que a execução anterior de Bob terminou. Inicia novamente a captura loopback.

Terminal 1:

```text
.venv/bin/python ferramentas/Diffie_Hellman/servidor.py --porta 5050 --segredo 7
```

Terminal 2:

```text
.venv/bin/python ferramentas/Diffie_Hellman/mitm.py --porta 6060 --porta-servidor 5050 --alterar
```

Terminal 3:

```text
.venv/bin/python ferramentas/Diffie_Hellman/cliente.py --porta 6060 --segredo 6 --mensagem "Autorizar envio do relatorio"
```

Guarda `03_dh_intermediario.pcapng`. Compara o texto enviado por Alice com o aceite por Bob, os segredos dos participantes e as duas ligações TCP.

**Prova:** valores públicos de uma troca, segredo recuperado pelo observador, diagnóstico da porta errada e mensagens antes/depois da intervenção.

**Conclui:** o segredo foi transmitido diretamente ou calculado? Porque o observador consegue recuperá-lo neste laboratório? O campo `texto` está cifrado? Um MAC válido prova a identidade de Alice quando a troca de chaves não é autenticada? Propõe uma forma de autenticar os participantes.

O intermediário é um proxy explícito: Alice liga deliberadamente à sua porta. Os parâmetros pequenos são didáticos. Este programa usa texto em claro com HMAC; não implementa um chat cifrado seguro.

## 4–6. Missão de hacking ético — auditar o portal

A empresa autorizou uma auditoria às três bancadas Web fornecidas. O contrato pede que investigues **ficheiros, login e perfis**, demonstres pelo menos **duas falhas diferentes** e confirmes as correções. Uma suspeita sem prova deve ficar identificada como suspeita.

### Contrato e regras de intervenção

- **Alvo autorizado:** exclusivamente as aplicações fornecidas em `http://127.0.0.1:5080/`, no teu computador. Os três serviços são executados um de cada vez.
- **Permitido:** navegar, observar pedidos no separador Network/Rede, alterar parâmetros do endereço, executar a ferramenta de tentativas fornecida e capturar o teu tráfego de laboratório.
- **Dados de teste:** contas e documentos fictícios. O ficheiro `root_secret.txt` da bancada de ficheiros foi colocado propositadamente fora da pasta pública e faz parte do âmbito.
- **Limite do login:** uma execução da lista fornecida por versão e um ensaio manual de até cinco falhas, seguido de uma tentativa correta. Aguarda cada resposta. Reinicia a aplicação antes do ensaio manual.
- **Fora do âmbito:** outros endereços/serviços, ficheiros do sistema ou pessoais, contas reais, eliminação de dados, persistência e testes de sobrecarga. Não aumentes a lista nem a velocidade das tentativas.
- Regista o que fizeste. Para quando tiveres a prova mínima: não precisas de recolher todos os dados disponíveis.

Não tens de programar, editar scripts ou criar pedidos em código. As ferramentas de programador do navegador servem aqui para observar a rede; não precisas de usar a consola JavaScript.

### Dossiê recebido

| Bancada | Informação inicial | Pergunta de auditoria |
|---|---|---|
| Ficheiros | Existe um relatório público; `root_secret.txt` deve permanecer fora do acesso público | O portal limita o acesso à pasta autorizada? |
| Login | Utilizador de teste: `alice`; há uma ferramenta de tentativas fornecida | A autenticação resiste ao ensaio autorizado? O transporte esconde as credenciais? |
| Perfis | Conta normal: `alice` / `a`; existe também o utilizador fictício `bob` | Um utilizador consegue consultar informação que não lhe pertence? |

As credenciais de Alice no serviço de perfis não são as credenciais do serviço de login. As bancadas não partilham dados, mesmo usando o mesmo endereço local.

### Preparar a bancada — comandos operacionais

Abre as ferramentas de programador do navegador, separador **Network/Rede**. Para registar redirecionamentos, ativa a preservação do registo. Nas capturas Wireshark usa a interface loopback e `tcp port 5080`.

Para cada bancada, inicia a versão inicial, investiga, guarda as provas e para o servidor com Ctrl+C. Inicia então a versão protegida e repete **os mesmos testes**, incluindo um uso legítimo. Antes de mudar de aplicação ou versão, fecha todas as janelas privadas e abre uma nova, ou limpa os cookies do endereço: abrir apenas mais uma janela privada pode reutilizar a sessão.

**Bancada de ficheiros:**

```text
.venv/bin/python -m flask --app ferramentas/Web/lab1_traversal/app.py run --host 127.0.0.1 --port 5080
```

Versão protegida:

```text
.venv/bin/python -m flask --app ferramentas/Web/lab1_traversal/app_secure.py run --host 127.0.0.1 --port 5080
```

**Bancada de login:**

```text
.venv/bin/python -m flask --app ferramentas/Web/lab2_bruteforce/app.py run --host 127.0.0.1 --port 5080
```

Versão protegida:

```text
.venv/bin/python -m flask --app ferramentas/Web/lab2_bruteforce/app_secure.py run --host 127.0.0.1 --port 5080
```

**Bancada de perfis:**

```text
.venv/bin/python -m flask --app ferramentas/Web/lab3_accesscontrol/app.py run --host 127.0.0.1 --port 5080
```

Versão protegida:

```text
.venv/bin/python -m flask --app ferramentas/Web/lab3_accesscontrol/app_secure.py run --host 127.0.0.1 --port 5080
```

### Investigar e demonstrar

Em cada bancada, começa por usar uma funcionalidade legítima e observa o endereço e os pedidos. Escreve uma hipótese antes de a testar. Decide que parâmetro, identidade ou sequência de tentativas deves comparar, dentro do contrato.

1. **Ficheiros:** estabelece um acesso público de referência; investiga se a seleção de ficheiros ultrapassa a pasta autorizada. Guarda o pedido exato e o resultado.
2. **Login:** localiza e executa a ferramenta de tentativas já fornecida. Identifica o que permite concluir e o que não testa. Observa um POST na captura e planeia um ensaio limitado que permita comparar a proteção das duas versões. Uma mensagem de sucesso nas duas não termina a investigação.
3. **Perfis:** compara o acesso sem sessão, com Alice ao próprio perfil e com Alice ao recurso de outro utilizador. Procura uma fronteira de permissões: uma recusa isolada não demonstra que todos os recursos estejam protegidos.

Se ficares bloqueado, consulta [as pistas graduais](PISTAS.md). Começa pelo nível 1 e regista o nível mais alto usado. Pedir uma pista não invalida o trabalho; explica como a usaste.

### Validar a correção

Para cada descoberta, repete na versão protegida o pedido ou a sequência exata que usaste. Confirma também que uma operação legítima continua a funcionar. Distingue «o meu teste deixou de funcionar» de «a aplicação inteira é segura».

**Provas mínimas da auditoria:**

- Registo de investigação das três bancadas, mesmo que um resultado fique inconclusivo.
- Pelo menos duas descobertas de natureza diferente, com pedido/ação reproduzível, identidade usada, resultado e impacto.
- Para cada descoberta, comparação antes/depois e um teste legítimo de controlo.
- Uma captura `05_login.pcapng` com a observação do transporte HTTP, acompanhada da explicação do que é visível.
- Uma conclusão sobre a diferença entre cifragem, autenticação e autorização.

Preenche as secções 4–6 da ficha. Se não confirmares uma falha, descreve o que testaste e o que falta investigar; não inventes resultados.

## 7. Reunião de resposta ao incidente

Apresenta a auditoria à direção com base nas provas recolhidas. A empresa só pode começar por três correções. Escolhe-as e, para cada uma, indica:

1. O problema observado e o recurso afetado.
2. A prova que recolheste.
3. A medida proposta e o que protege.
4. Um novo teste que demonstraria a correção e um acesso legítimo que deve continuar a funcionar.

Responde à direção: **«Se colocarmos HTTPS no portal e AES no chat, todas as falhas que demonstrámos desaparecem?»** Usa três resultados diferentes da vossa investigação.

Entrega a ficha e as evidências. Não precisas de entregar código.
