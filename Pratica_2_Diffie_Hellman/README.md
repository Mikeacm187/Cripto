# Consegues combinar um segredo debaixo de escuta?

Laboratório prático de redes sobre Diffie-Hellman. Vais ligar dois computadores, analisar a troca no Wireshark, diagnosticar uma avaria e testar um intermediário ativo.

**Não precisas de programar:** todos os ficheiros Python estão prontos. Vais executar comandos, recolher capturas e explicar os resultados.

## Começa aqui

1. Abre a [ficha de trabalho](alunos/Guia_Aluno.md).
2. Consulta a [preparação do posto](alunos/Preparacao.md).
3. Na página principal do repositório, seleciona **Code > Download ZIP** e extrai o ficheiro.
4. Abre a pasta `Pratica_2_Diffie_Hellman/alunos` e inicia aí o terminal.
5. Segue os desafios da ficha. Para uma versão de impressão, abre `Guia_Aluno.html` no navegador do computador.

Precisas de Python 3.10 ou superior e Wireshark. Não é necessário instalar bibliotecas Python adicionais. No Windows usa `py -3`; em macOS/Linux usa `python3`.

## Ficheiros

| Ficheiro | Papel |
| --- | --- |
| `servidor.py` | Bob: escuta e recebe a ligação TCP. |
| `cliente.py` | Alice: liga a Bob e inicia a troca. |
| `comum.py` | Funções partilhadas pelos programas; mantém na mesma pasta. |
| `observador.py` | Tenta recuperar o segredo a partir dos valores públicos do exemplo. |
| `mitm.py` | Intermediário explícito para o último desafio. |

## Percurso

1. Põe o serviço online.
2. Descobre o que passou no fio.
3. Explica como os PCs obtiveram o mesmo segredo.
4. Tenta recuperar esse segredo.
5. Diagnostica um incidente e prova a recuperação.
6. Testa o intermediário ativo (extensão).

O percurso base demora cerca de 90 minutos; a extensão acrescenta cerca de 25 minutos.

## Entrega

Segue a lista no final da ficha. Entrega as respostas e as capturas pelo canal indicado na aula. Não publiques capturas ou respostas neste repositório.

## Limites do exemplo

Usa apenas os postos e a rede atribuídos à aula. Os números são pequenos de propósito. O programa transmite texto em claro com HMAC, sem cifragem e sem autenticação da identidade. Não serve para proteger informação real. O MITM é um proxy configurado explicitamente, sem alteração de ARP, DNS ou encaminhamento da rede.

Base curricular: Aula 3, Protocolo Diffie-Hellman.
