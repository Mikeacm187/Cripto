# Operação Rede em Risco

Laboratório integrado de redes, criptografia e segurança Web · Trabalho em pares

Uma empresa fictícia comunica através de um chat antigo e guarda documentos numa aplicação Web. A direção diz: «Temos cifras e palavras-passe, por isso estamos seguros.» A vossa equipa tem de testar essa afirmação e recomendar correções com provas.

As aplicações são bancadas separadas da mesma auditoria: não partilham utilizadores, sessões ou chaves. O cenário liga os resultados; não existe uma cadeia automática em que uma ferramenta desbloqueia a seguinte.

**Objetivo:** realizar uma auditoria de hacking ético, demonstrar falhas com provas e validar correções nas bancadas fornecidas. Na missão Web, investigas as três bancadas e documentas pelo menos duas descobertas diferentes.

**Não tens de programar, completar funções nem editar ficheiros Python.** Só vais executar comandos, introduzir dados nas ferramentas, usar o navegador e o Wireshark e responder na ficha. Copiar um comando de execução não implica compreender o código do programa.

## Preparação

Extrai o ZIP e abre um terminal na pasta `alunos` que contém este documento. Precisas de Python 3.10 ou posterior e Wireshark. Usa apenas dados fictícios e as aplicações fornecidas; a componente Web fica em localhost. O chat só deve ser usado na rede de laboratório autorizada.

Windows, PowerShell ou CMD:

```text
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS/Linux:

```text
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

**Convenção nos documentos:** os exemplos usam `.venv/bin/python`, para macOS/Linux. No Windows substitui esse início por `.venv\Scripts\python.exe`. Mantém o resto do comando igual. Não precisas de ativar o ambiente virtual. Em cada terminal novo, abre novamente a pasta `alunos`; mantém todos os terminais nessa pasta.

## Organização

- Abre `MISSAO.html` para seguir os desafios e o contrato da auditoria Web.
- Se precisares de apoio na investigação, usa `PISTAS.html`, começando pelo nível 1.
- Regista os resultados em `FICHA_RESPOSTAS.md` ou num documento à tua escolha.
- Cria uma pasta `evidencias` para as capturas.
- Um elemento opera e o outro recolhe provas; troquem de função a meio.
- Interrompe um servidor com Ctrl+C antes de iniciar o seguinte.

| Serviço | Porta | Local |
|---|---:|---|
| Chat por substituição | 5001 | Mesmo computador ou rede de laboratório |
| Bob / Diffie–Hellman | 5050 | Mesmo computador |
| Mallory / intermediário explícito | 6060 | Mesmo computador |
| Aplicações Web, uma de cada vez | 5080 | Mesmo computador |

No mesmo computador, usa `127.0.0.1` como destino. No Wireshark, captura na interface loopback: `lo0` no Mac, `lo` no Linux ou o adaptador de loopback Npcap no Windows. Se não existir no Windows, confirma que o suporte Npcap está instalado; pede apoio à docente. Para o chat entre computadores, usa a interface de rede ativa e substitui o destino pelo IPv4 real do servidor.

**Filtros de captura:** `tcp port 5001`, `tcp port 5050 or tcp port 6060` ou `tcp port 5080`.

**Filtros de visualização:** `tcp.port == 5001`, `tcp.port == 5050 || tcp.port == 6060` ou `tcp.port == 5080`.

## Se algo falhar

- «Ficheiro não encontrado»: confirma que estás na pasta `alunos`.
- «No module named ...»: repete a instalação com o Python do ambiente virtual.
- «Connection refused»: verifica se o servidor arrancou, o IP e a porta.
- «Timed out»: verifica IP, serviço e regras da rede; não desligues a firewall indiscriminadamente.
- «Address already in use»: encerra a execução anterior. As portas do guião já evitam a 5000.
- Não aparece tráfego: confirma a interface, inicia a captura antes da experiência e verifica o filtro.
- Para veres o conteúdo TCP: seleciona um pacote e usa **Follow > TCP Stream**. Ao mudar de conversa, remove o filtro de stream anterior.
- Se uma instalação bloquear o grupo, usa o posto preparado pela docente para recolher a prova e continua a análise. Regista essa alternativa.

## Entrega

Submete um ZIP com a ficha preenchida e as evidências. Não incluas `.venv`, os programas fornecidos ou dados reais. Cada conclusão deve indicar a evidência que a suporta. Uma captura sem explicação não fecha o diagnóstico.
