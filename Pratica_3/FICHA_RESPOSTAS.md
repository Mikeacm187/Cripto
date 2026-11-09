# Operação Rede em Risco — relatório de investigação

Grupo: ___ · Elementos: ___ · Data: ___

Em cada prova, indica o nome do ficheiro e o pacote/linha relevante. Cola apenas os excertos necessários e explica o que demonstram.

## 1. Comunicações antigas

- Previsão inicial: ___
- IP/porta de origem e IP/porta de destino no chat: ___
- Mensagem original e conteúdo observado na captura: ___
- Chave e mensagem recuperada por César: ___
- Resultado Vigenère e confirmação por recifragem: ___
- Diferença entre os três mecanismos e consequências de divulgar o mapa: ___
- Decifrar com chave conhecida é o mesmo que quebrar sem chave? ___
- Evidências: ___

## 2. AES e dados armazenados

| Entrada | Caracteres | Bytes UTF-8 | Bytes de padding | Total após padding |
|---|---:|---:|---:|---:|
| Olá! | | | | |
| 16 letras A | | | | |

| Modo | Tem IV? | Blocos afetados após alteração de um bit | Autentica os dados por si só? |
|---|---|---|---|
| ECB | | | |
| CBC | | | |
| CFB-128 | | | |
| OFB | | | |

- Previsão e resultado dos blocos repetidos: ___
- Efeito de alterar o IV: ___
- Diferença entre bloco e chave; comparação DES/AES: ___
- Decifragem sem erro ou padding válido prova integridade? ___
- Evidências: ___

## 3. Rede, Diffie–Hellman e intermediário

- Previsão: ___
- Pacotes SYN / SYN-ACK / ACK: ___
- p / g / A / B na ligação direta: ___
- Segredos locais de Alice e Bob; resultado do observador: ___
- O texto estava cifrado? Evidência: ___
- Erro com a porta 5051 e correção: ___

| Observação | Ligação direta | Com intermediário |
|---|---|---|
| Texto enviado por Alice | | |
| Texto aceite por Bob | | |
| K de Alice | | |
| K de Bob | | |
| K de Mallory com Alice/Bob | Não aplicável | |
| Número de ligações TCP e portas | | |

- Porque o observador recuperou o segredo? ___
- Porque um MAC válido não impediu esta intervenção? ___
- Proposta de autenticação da troca: ___
- Evidências: ___

## 4–6. Relatório de auditoria de hacking ético

Confirmámos o âmbito e os limites do contrato: ___

### Registo de investigação das três bancadas

| Bancada | Hipótese antes do teste | Ação/pedido e identidade | Observação | Confirmado/inconclusivo | Pista máxima usada |
|---|---|---|---|---|---|
| Ficheiros | | | | | |
| Login | | | | | |
| Perfis | | | | | |

### Descoberta 1

- Título e bancada: ___
- Recurso e propriedade de segurança afetados: ___
- Identidade utilizada e acesso que devia ter: ___
- Passos exatos para reproduzir, dentro do âmbito: ___
- Pedido/ação e resultado na versão inicial (inclui HTTP quando aplicável): ___
- Impacto demonstrado; consequências hipotéticas claramente separadas: ___
- Evidência (ficheiro e pacote/linha/pedido): ___
- Correção proposta e justificação: ___
- Mesmo teste na versão protegida e resultado: ___
- Operação legítima de controlo e resultado: ___
- Limites desta prova: ___

### Descoberta 2

- Título e bancada: ___
- Recurso e propriedade de segurança afetados: ___
- Identidade utilizada e acesso que devia ter: ___
- Passos exatos para reproduzir, dentro do âmbito: ___
- Pedido/ação e resultado na versão inicial (inclui HTTP quando aplicável): ___
- Impacto demonstrado; consequências hipotéticas claramente separadas: ___
- Evidência (ficheiro e pacote/linha/pedido): ___
- Correção proposta e justificação: ___
- Mesmo teste na versão protegida e resultado: ___
- Operação legítima de controlo e resultado: ___
- Limites desta prova: ___

Duplica a estrutura se confirmares outras descobertas.

### Transporte e autenticação

- Ficheiro `05_login.pcapng` e pacote/stream relevante: ___
- O que conseguiste observar no POST HTTP? ___
- Resultado da lista original nas duas versões; o que concluis? ___
- Ensaio manual limitado, número de falhas e resultado: ___
- O que HTTPS resolveria e que falhas permaneceriam? ___
- Diferença entre autenticação e autorização, com uma prova desta auditoria: ___

## 7. Decisão da equipa

| Prioridade | Problema e recurso | Evidência | Correção proposta | Teste de correção e acesso legítimo a manter |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

«HTTPS no portal e AES no chat resolvem todas as falhas?» Justifica com três resultados: ___

Limitações ou tarefas não concluídas: ___
