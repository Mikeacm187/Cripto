# Preparação do posto

1. Usa Python 3.10 ou superior e Wireshark. Não são necessárias bibliotecas Python adicionais.
2. Extrai a pasta alunos. No Windows, abre essa pasta no Explorador, escreve powershell na barra de endereço e prime Enter. No macOS/Linux, abre o Terminal, escreve `cd `, arrasta a pasta alunos para a janela e prime Enter.
3. Confirma a versão: Windows `py -3 --version`; macOS/Linux `python3 --version`.
4. Nos comandos da ficha, substitui `python3` por `py -3` se usares Windows.
5. Para capturar no mesmo PC, seleciona a interface loopback: lo no Linux, lo0 no macOS ou a interface loopback do Npcap no Windows. Entre PCs, captura na interface Ethernet/Wi-Fi da ligação.
6. Executa os comandos na pasta alunos. Para terminar um programa, prime Ctrl+C. Cada execução do servidor aceita uma ligação: reinicia-o antes de repetir.

## Se não conseguires avançar

- Ficheiro não encontrado: confirma a pasta do terminal.
- Endereço em uso: termina o servidor anterior.
- Captura vazia: confirma a interface, os filtros e o início da captura antes do cliente.
- Entre PCs sem ligação: confirma IP, porta, interface de escuta e eventuais restrições da rede da aula.

## Condições da experiência

Usa apenas os computadores e a rede atribuídos à atividade. O código usa números pequenos, transmite texto em claro e não serve para proteger informação real. O intermediário é um proxy ao qual o cliente liga explicitamente; não altera ARP, DNS nem encaminhamento da rede.
