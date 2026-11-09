import os
from collections import Counter
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def blocos(dados):
    return [dados[i:i + 16] for i in range(0, len(dados), 16)]

def processar(dados, chave, modo, decifrar=False):
    cifra = Cipher(algorithms.AES(chave), modo)
    contexto = cifra.decryptor() if decifrar else cifra.encryptor()
    return contexto.update(dados) + contexto.finalize()

def mostrar(nome, ct):
    print(f"\n{nome}:")
    lista = blocos(ct)
    for i, bloco in enumerate(lista, 1):
        print(f"Bloco {i}: {bloco.hex()}")
    contagens = Counter(lista)
    print("Blocos distintos:", len(contagens))
    print("Grupos de blocos repetidos:", sum(n > 1 for n in contagens.values()))

def main():
    chave, iv = os.urandom(16), os.urandom(16)
    dados = b"A" * 64
    # Sem padding: os 64 bytes ja formam quatro blocos.
    ecb = processar(dados, chave, modes.ECB())
    cbc = processar(dados, chave, modes.CBC(iv))
    mostrar("ECB", ecb)
    mostrar("CBC", cbc)
    assert processar(ecb, chave, modes.ECB(), True) == dados
    assert processar(cbc, chave, modes.CBC(iv), True) == dados
    outro_iv = os.urandom(16)
    while outro_iv == iv:
        outro_iv = os.urandom(16)
    cbc_novo = processar(dados, chave, modes.CBC(outro_iv))
    print("\nCBC com outro IV e diferente:", cbc_novo != cbc)
    repetido = processar(dados, chave, modes.CBC(iv))
    print("CBC com a mesma chave, IV e dados e igual:", repetido == cbc)
    # Reutilizacao do IV exclusivamente na comparacao controlada.
    alterados = b"B" + dados[1:]
    for nome, modo, original in (("ECB", modes.ECB(), ecb),
                                  ("CBC", modes.CBC(iv), cbc)):
        novo = processar(alterados, chave, modo)
        indices = [i + 1 for i, (a, b) in enumerate(
            zip(blocos(original), blocos(novo))) if a != b]
        print(nome, "blocos alterados ao mudar o byte 0:", indices)
    mensagem = "Seguranca em acao!".encode("utf-8")
    p = padding.PKCS7(128).padder()
    completos = p.update(mensagem) + p.finalize()
    novo_iv = os.urandom(16)
    ct = processar(completos, chave, modes.CBC(novo_iv))
    brutos = processar(ct, chave, modes.CBC(novo_iv), True)
    u = padding.PKCS7(128).unpadder()
    recuperados = u.update(brutos) + u.finalize()
    assert recuperados == mensagem
    print("CBC com mensagem arbitraria e PKCS#7: OK")

if __name__ == "__main__":
    main()
