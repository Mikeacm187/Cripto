# Relatório - Laboratório de Criptografia

**Elemento 1 - nome e número:**  
**Elemento 2 - nome e número:**  
**Turma:**  
**Data:**  
**Versão de Python:**  
**Versão de cryptography:**  

> Preencher este documento com as observações do grupo. Podem copiar a estrutura
> para Word ou LibreOffice e exportar para PDF. Substituir os campos «A preencher».

## 1. César por força bruta

- Mensagem recuperada: A preencher.
- Chave identificada: A preencher.
- Como recuperámos a mensagem: A preencher.
- Porque foi viável testar as chaves: A preencher.
- Adequação para informação confidencial: A preencher.
- Evidência (nome do ficheiro): A preencher.

## 2. Ferramenta César

| Mensagem original | Chave | Mensagem cifrada | Recuperação exata? |
|---|---|---|---|
| A preencher | | | |
| A preencher | | | |
| A preencher | | | |

- Efeito nos acentos, espaços e pontuação: A preencher.
- Mensagem recebida do outro grupo (ou alternativa indicada pela docente): A preencher.
- Mensagem recuperada e chave: A preencher.
- Método usado e principal fragilidade: A preencher.
- Evidências: A preencher.

## 3. DES, AES, blocos e padding

| Característica | DES | AES |
|---|---|---|
| Tipo de criptografia | | |
| Tamanho do bloco | | |
| Tamanho da chave | | |
| Número de rondas | | |
| Segurança | | |

| Mensagem | Caracteres | Bytes originais | Bytes acrescentados | Valor do padding | Total final |
|---|---|---|---|---|---|
| Olá! | | | | | |
| 16 letras A | | | | | |
| 17 letras A | | | | | |
| Vazia | | | | | |

1. Diferença entre caracteres e bytes: A preencher.
2. Função do padding: A preencher.
3. Mensagens de 16 bytes e vazias: A preencher.
4. Diferença entre tamanho do bloco e da chave: A preencher.
5. Razão da insegurança do DES: A preencher.
6. AES simétrico ou assimétrico e justificação: A preencher.

Fontes consultadas e evidências: A preencher.

## 4. AES em ECB e CBC

| Experiência | Observação ECB | Observação CBC |
|---|---|---|
| Blocos repetidos | | |
| Alterar o IV | Não aplicável | |
| Repetir mensagem, chave e IV | Não utiliza IV | |
| Alterar o primeiro byte da mensagem | | |

1. Exposição de padrões em ECB: A preencher.
2. Função do IV: A preencher.
3. Efeito de repetir mensagem, chave e IV: A preencher.
4. Proteção contra repetições: A preencher.
5. CBC e deteção de alterações: A preencher.

Comparação das imagens (opcional): A preencher ou indicar «não realizada».

Evidências: A preencher.

## 5. Comparação dos modos

| Modo | Recuperação original | Blocos afetados | Bits diferentes no texto recuperado | Observação |
|---|---|---|---|---|
| ECB | | | | |
| CBC | | | | |
| CFB | | | | |
| OFB | | | | |

| Característica | ECB | CBC | CFB | OFB |
|---|---|---|---|---|
| Necessita de IV? | | | | |
| Oculta padrões repetidos? | | | | |
| Necessita de padding? | | | | |
| Encadeamento ou feedback? | | | | |
| Propagação de um bit alterado no criptograma | | | | |
| Garante integridade e autenticação isoladamente? | | | | |

- Alteração aplicada e alterações observadas: A preencher.
- Localização e propagação dos efeitos: A preencher.
- Significado de um padding válido: A preencher.
- Integridade e autenticação dos modos: A preencher.
- Evidências: A preencher.

### Decisão de segurança

| Cenário | Requisitos | Mecanismo proposto | Justificação | Limitação |
|---|---|---|---|---|
| A - Ficheiros confidenciais | | | | |
| B - Comunicação em rede | | | | |
| C - Deteção de alterações | | | | |

Diferença entre confidencialidade, integridade e autenticação: A preencher.

## 6. Missão final e conclusão

Que mecanismos escolheríamos para uma aplicação com informação confidencial e porquê?

A preencher com referência às experiências realizadas.

## 7. Fontes consultadas

Registar os títulos, ligações e datas de consulta das fontes usadas.

A preencher.
