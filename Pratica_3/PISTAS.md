# Apoio à auditoria — pistas graduais

Usa apenas a ajuda de que precisas. Lê o nível 1 antes do 2 e o 2 antes do 3. Regista o nível mais alto usado em cada bancada. Todos os testes continuam limitados ao contrato em `MISSAO.html`.

## Nível 1 — observar e formular uma hipótese

**Ficheiros:** abre o relatório público pelo link da página. Que parte do endereço parece selecionar o ficheiro? Que pasta deveria limitar os documentos acessíveis?

**Login:** procura na pasta de ferramentas um programa que experimente palavras-passe. Observa quantas tentativas faz até obter sucesso. Um teste que termina cedo permite avaliar todos os mecanismos de bloqueio?

**Perfis:** inicia sessão como Alice. Abre o perfil disponibilizado pela página e observa o endereço. A identidade da sessão e o recurso selecionado no endereço são necessariamente a mesma coisa?

## Nível 2 — escolher o teste

**Ficheiros:** o parâmetro `name` controla a seleção do documento. Em caminhos de ficheiros, `..` representa a pasta acima. O contrato autoriza apenas o documento fictício `root_secret.txt`, além do relatório público; não procures ficheiros pessoais ou do sistema.

**Login:** a ferramenta existente executa-se num segundo terminal, com a aplicação de login já iniciada:

```text
.venv/bin/python ferramentas/Web/lab2_bruteforce/try_passwords.py
```

Em Windows substitui o início por `.venv\Scripts\python.exe`. Não edites o programa. Compara a lista original nas duas versões. Para avaliar o bloqueio, reinicia cada aplicação e planeia o ensaio manual permitido: até cinco falhas, seguidas da palavra-passe encontrada. Na captura de rede, procura o POST e o seu corpo.

**Perfis:** compara o acesso ao mesmo recurso sem sessão e com Alice autenticada. Depois compara o recurso de Alice com o de Bob. Usa o separador Network/Rede para distinguir dados devolvidos, recusa e redirecionamento.

## Nível 3 — desbloquear a experiência

**Ficheiros:** compara os pedidos seguintes nas duas versões:

```text
http://127.0.0.1:5080/download?name=report.txt
http://127.0.0.1:5080/download?name=../root_secret.txt
```

Regista o pedido exato, o conteúdo e o estado HTTP; mantém o acesso ao relatório público como controlo legítimo. Não avances para outros caminhos.

**Login:** a lista original pode acertar antes de atingir o limiar de bloqueio. Depois de reiniciar a aplicação, introduz cinco palavras-passe erradas para `alice`, uma de cada vez, aguardando as respostas. Logo a seguir, experimenta a palavra-passe correta que a ferramenta encontrou. Repete na outra versão, também reiniciada. Não ultrapasses esta sequência. Se precisares da credencial de teste para concluir, pede-a à docente.

**Perfis:** numa sessão de Alice (`alice` / `a`), compara:

```text
http://127.0.0.1:5080/profile?user=alice
http://127.0.0.1:5080/profile?user=bob
```

Fecha todas as janelas privadas e abre outra para testar o perfil de Bob sem sessão, ou limpa os cookies do endereço. Repete na versão protegida. Um resultado permitido na versão inicial e recusado na protegida precisa de uma explicação sobre quem deveria aceder ao recurso.

## Se já tens uma prova

Para de explorar esse recurso. Documenta o impacto demonstrado, propõe uma correção e repete o teste na versão protegida. Verifica também o uso legítimo. A pista ajuda a executar; a conclusão e a justificação são da tua equipa.
