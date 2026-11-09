# Laboratório de Criptografia

## Executar, experimentar e interpretar

**Unidade curricular:** Criptografia e Segurança Informática  
**Modalidade:** grupos de 2 estudantes  
**Ferramenta:** Python 3.10 ou superior  
**Conhecimentos de programação:** não são necessários.

Vão trabalhar como uma equipa de analistas de segurança: executar ferramentas,
observar os resultados e explicar as suas implicações. Os programas estão completos.
Não precisam de construir funções, implementar algoritmos ou completar código.

O trabalho tem cinco desafios. O objetivo é compreender os resultados e justificar
as conclusões, não decorar o código. Alterações ao código são opcionais.
Utilizem apenas as mensagens e os ficheiros de teste deste laboratório.

## 1. Preparar o ambiente

1. Descarregar este repositório em **Code > Download ZIP** e extrair a pasta.
2. Abrir a pasta no Visual Studio Code ou noutro editor.
3. Abrir um terminal nessa pasta (**Terminal > New Terminal** no VS Code).
4. Verificar o Python e criar um ambiente virtual:

```bash
python --version
python -m venv .venv
```

Ativar o ambiente:

**Windows / PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

Se a ativação estiver bloqueada, podem instalar e executar diretamente através
 de `.venv\Scripts\python.exe`, substituindo `python` nos comandos seguintes.
Não é necessário alterar as políticas de segurança do computador.

**macOS / Linux**

```bash
source .venv/bin/activate
```

Em sistemas onde `python` não existe, usar `python3` para verificar a versão e
criar o ambiente. Após a ativação, usar o comando disponibilizado nesse ambiente.

Instalar a biblioteca:

```bash
python -m pip install -r requirements.txt
```

Os comandos seguintes são executados a partir da pasta principal do projeto.
Se aparecer «No module named cryptography», confirmem que instalaram a biblioteca
com o mesmo Python que está a executar o programa.

## 2. Organizar o trabalho

```text
challenge-01/caesar_breaker.py     Candidatos da cifra de César
challenge-02/cipher_tool.py        Ferramenta interativa de César
challenge-03/block_ciphers.py      Bytes, blocos e preenchimento
challenge-04/aes_modes.py          Experiências ECB e CBC
challenge-04/bonus_bmp.py          Experiência visual opcional
challenge-05/modes_comparison.py   Comparação dos quatro modos
report/relatorio.md               Modelo de relatório a preencher
report/COMO_EXPORTAR_PDF.md        Instruções para criar o PDF
evidence/                       Guardar capturas e outros resultados
```

Registem as respostas no modelo de relatório. A pasta de evidências começa vazia:
guardem nela as vossas capturas de ecrã, identificadas pelo desafio. Não é preciso
compreender cada linha dos programas para realizar as experiências.

## Desafio 01 - Descobrir a mensagem

Uma mensagem foi cifrada com a cifra de César, mas desconhece-se a chave:

```text
D VHJXUDQFD GRV GDGRV H HVVHQFLDO
```

Executar:

```bash
python challenge-01/caesar_breaker.py
```

O programa apresenta 26 candidatos, um para cada chave de 0 a 25.

**O que fazer**

1. Ler os candidatos e encontrar uma mensagem com significado.
2. Registar a mensagem e a chave correspondente.
3. Guardar uma captura com o resultado identificado.

**Responder**

- Como conseguiram recuperar a mensagem sem conhecer a chave?
- Porque é que testar todas as chaves é viável neste caso?
- Usariam esta cifra para proteger informação confidencial? Justifiquem.

## Desafio 02 - Experimentar a ferramenta César

Executar:

```bash
python challenge-02/cipher_tool.py
```

O programa apresenta um menu: cifrar, decifrar, testar todas as chaves e sair.
Introduzam as mensagens e as chaves quando forem solicitadas. Não precisam de
alterar o programa. Se uma entrada for inválida, o programa permite tentar novamente.

**O que fazer**

1. Cifrar três mensagens à vossa escolha, com chaves distintas.
2. Decifrar cada resultado com a mesma chave e comparar com o original.
3. Incluir pelo menos uma mensagem com espaços, pontuação e letras acentuadas.
4. Trocar uma mensagem cifrada com outro grupo, sem revelar a chave.
5. Utilizar a opção de força bruta para tentar recuperar a mensagem recebida.

Só as letras A-Z e a-z são deslocadas. As letras acentuadas e os restantes
caracteres mantêm-se inalterados. O programa aceita chaves inteiras, incluindo
negativas, e converte-as para o intervalo equivalente de 0 a 25.

**Responder**

- A decifragem recuperou exatamente as três mensagens?
- O que aconteceu aos acentos, espaços e sinais de pontuação?
- Conseguiram descobrir a mensagem do outro grupo? Como?
- Qual é a principal fragilidade desta ferramenta enquanto mecanismo de segurança?

Se não houver outro grupo disponível, peçam à docente uma mensagem de teste e
registem essa alternativa no relatório.

## Desafio 03 - DES, AES, blocos e padding

### A. Investigar

Consultar as referências no final e completar no relatório a comparação DES/AES:
tipo de criptografia, tamanho do bloco, tamanho da chave, número de rondas e segurança.
Não é necessário implementar DES nem AES.

### B. Observar o programa

Executar estes quatro exemplos, um de cada vez:

```bash
python challenge-03/block_ciphers.py "Olá!"
python challenge-03/block_ciphers.py "AAAAAAAAAAAAAAAA"
python challenge-03/block_ciphers.py "AAAAAAAAAAAAAAAAA"
python challenge-03/block_ciphers.py ""
```

Podem também executar sem argumento e escrever uma mensagem quando for pedida:

```bash
python challenge-03/block_ciphers.py
```

O programa mostra o número de caracteres e bytes, divide os dados em blocos de
16 bytes, aplica PKCS#7 e verifica a remoção do preenchimento.

**O que fazer**

- Registar, para cada exemplo, o número de bytes antes e depois do padding.
- Identificar quantos bytes foram acrescentados e o respetivo valor.
- Comparar uma mensagem com 16 letras A com outra de 17 letras A.

**Responder**

1. Porque pode o número de bytes ser diferente do número de caracteres?
2. Para que serve o padding em determinados modos de cifragem?
3. O que acontece quando a mensagem já tem exatamente 16 bytes? E se estiver vazia?
4. Qual é a diferença entre tamanho do bloco e tamanho da chave?
5. Porque deixou o DES de ser uma escolha segura?
6. O AES é simétrico ou assimétrico? Justifiquem.

## Desafio 04 - Comparar AES em ECB e CBC

Executar:

```bash
python challenge-04/aes_modes.py
```

O programa faz automaticamente as experiências: cifra quatro blocos iguais,
mostra os blocos de saída, altera o IV, repete uma cifragem e altera o primeiro
byte da mensagem. No final, testa também CBC com padding.

**Como ler a saída**

- Cada bloco surge em hexadecimal: comparem as sequências visualmente.
- «Blocos distintos» conta quantos valores de bloco diferentes foram produzidos.
- `True` significa que a afirmação apresentada foi confirmada nessa execução.
- A lista de blocos alterados usa numeração a partir de 1.
- As chaves e os IV são aleatórios: os valores hexadecimais podem mudar entre execuções.

**O que fazer**

1. Identificar os blocos iguais em ECB e comparar com CBC.
2. Registar o efeito da alteração do IV.
3. Registar o resultado de repetir a mesma mensagem com a mesma chave e IV.
4. Comparar os blocos afetados quando se altera o primeiro byte da mensagem.
5. Guardar capturas que sustentem as observações.

**Responder**

1. Porque é que ECB pode revelar padrões?
2. Para que serve o IV em CBC?
3. O que acontece com a mesma mensagem, chave e IV?
4. Qual dos dois modos oculta melhor as repetições nesta experiência?
5. CBC permite garantir que uma mensagem não foi alterada? Justifiquem.

### Experiência visual opcional

```bash
python challenge-04/bonus_bmp.py
```

Abrir `original.bmp`, `ecb.bmp` e `cbc.bmp` na pasta `evidence/bmp/`.
O programa cria os ficheiros; não precisam de procurar nem editar uma imagem.
Comparar o que ainda se consegue reconhecer e explicar porquê.
Este é um exemplo didático que preserva o cabeçalho do BMP.

## Desafio 05 - Alterações e decisões de segurança

Executar:

```bash
python challenge-05/modes_comparison.py
```

O programa cifra e decifra com ECB, CBC, CFB e OFB. Depois altera automaticamente
um bit do criptograma e volta a decifrar. Não precisam de implementar a alteração.
CFB utiliza feedback de 128 bits, não CFB8.

**Como ler a saída**

- «Recuperação original: OK» confirma o teste antes da alteração.
- «Índices de bytes diferentes» identifica posições a partir de 0.
- «Blocos afetados» usa numeração a partir de 1.
- «Bits diferentes» refere-se ao texto recuperado, não ao criptograma adulterado.
- «Padding válido» não significa, por si só, que o conteúdo é autêntico.

Os dados corrompidos são apresentados em hexadecimal. O número exato de bits
alterados pode variar entre execuções. Comparem sobretudo a localização e a
propagação dos efeitos.

**O que fazer**

1. Confirmar a recuperação original nos quatro modos.
2. Registar quais os blocos afetados pela adulteração em cada modo.
3. Completar a tabela dos modos no relatório.

**Responder**

- Qual é a diferença entre a alteração aplicada e as alterações observadas?
- O efeito fica localizado ou propaga-se a outros blocos?
- Um padding válido garante que a mensagem não foi alterada?
- Algum destes quatro modos garante, por si só, integridade e autenticação?

### Decisão de segurança

Para cada cenário, identificar os requisitos, propor um mecanismo, justificar a
escolha e indicar uma limitação:

- **A:** documentos confidenciais armazenados num servidor.
- **B:** mensagens transmitidas através de uma rede.
- **C:** informação cuja alteração não autorizada deve ser detetada.

A escolha pode recorrer a mecanismos que acrescentem autenticação aos dados,
mesmo que não tenham sido implementados neste laboratório. Consultem as fontes
e distingam confidencialidade, integridade e autenticação.

## Missão final

Se fossem responsáveis pela segurança de uma aplicação que processa informação
confidencial, que mecanismos escolheriam e porquê? Fundamentem a resposta nas
experiências, nos requisitos e nas vulnerabilidades identificadas.

## Entrega no Moodle

Submeter um único ZIP com:

- Os programas fornecidos, organizados nas pastas originais.
- O relatório preenchido, exportado para `report/report.pdf`.
- Capturas de ecrã das execuções e resultados em `evidence/`.

Identificar os dois elementos do grupo no relatório. Não é necessário modificar
o código para cumprir o trabalho. Se o alterarem opcionalmente, descrevam o que
mudaram. Não incluir `.venv`, caches, palavras-passe ou informação confidencial.
Antes de entregar, extrair o ZIP e confirmar que os ficheiros estão presentes.
O commit no GitHub não substitui a entrega no Moodle.

## Referências de apoio

- [NIST: AES, FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)
- [NIST: DES, FIPS 46-3, norma retirada](https://csrc.nist.gov/pubs/fips/46-3/final)
- [NIST: modos de operação, SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final)
- [cryptography: cifragem simétrica](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)
- [cryptography: cifragem autenticada](https://cryptography.io/en/latest/hazmat/primitives/aead/)

Os modos estudados são usados para aprendizagem. Para proteger dados reais,
devem ser selecionados mecanismos adequados que também detetem adulteração.
