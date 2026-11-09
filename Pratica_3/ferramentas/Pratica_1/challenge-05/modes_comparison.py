import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
try:
    from cryptography.hazmat.decrepit.ciphers.modes import CFB, OFB
except ImportError:
    from cryptography.hazmat.primitives.ciphers.modes import CFB, OFB

def modo_para(nome, iv):
    if nome == "ECB":
        return modes.ECB()
    if nome == "CBC":
        return modes.CBC(iv)
    if nome == "CFB":
        return CFB(iv)  # Feedback de 128 bits.
    if nome == "OFB":
        return OFB(iv)
    raise ValueError("Modo desconhecido.")

def processar(dados, chave, nome, iv, decifrar=False):
    cifra = Cipher(algorithms.AES(chave), modo_para(nome, iv))
    ctx = cifra.decryptor() if decifrar else cifra.encryptor()
    return ctx.update(dados) + ctx.finalize()

def preencher(dados):
    p = padding.PKCS7(128).padder()
    return p.update(dados) + p.finalize()

def remover(dados):
    u = padding.PKCS7(128).unpadder()
    return u.update(dados) + u.finalize()

def alterar_bit(dados, posicao=0):
    if not 0 <= posicao < len(dados):
        raise ValueError("Posicao fora do criptograma.")
    alterado = bytearray(dados)
    # Troca apenas o bit menos significativo, sem operadores bit a bit.
    alterado[posicao] += 1 if alterado[posicao] % 2 == 0 else -1
    return bytes(alterado)

def diferencas(a, b):
    return [i for i, (x, y) in enumerate(zip(a, b)) if x != y]

def bits_diferentes(a, b):
    return sum((x // (2 ** k)) % 2 != (y // (2 ** k)) % 2
               for x, y in zip(a, b) for k in range(8))

def experiencia(nome, dados, chave):
    iv = None if nome == "ECB" else os.urandom(16)
    entrada = preencher(dados) if nome in {"ECB", "CBC"} else dados
    ct = processar(entrada, chave, nome, iv)
    bruto = processar(ct, chave, nome, iv, True)
    original = remover(bruto) if nome in {"ECB", "CBC"} else bruto
    assert original == dados
    adulterado = alterar_bit(ct)
    assert bits_diferentes(ct, adulterado) == 1
    corrompido = processar(adulterado, chave, nome, iv, True)
    indices = diferencas(entrada, corrompido)
    blocos = sorted({i // 16 + 1 for i in indices})
    print(f"\n{nome} | recuperacao original: OK")
    print("Criptograma:", ct.hex())
    print("Decifragem apos alteracao (hex):", corrompido.hex())
    print("Indices de bytes diferentes (base 0):", indices)
    print("Blocos afetados (base 1):", blocos)
    print("Bits diferentes no texto recuperado:",
          bits_diferentes(entrada, corrompido))
    if nome in {"ECB", "CBC"}:
        try:
            remover(corrompido)
            print("Padding valido apesar da adulteracao.")
        except ValueError:
            print("Padding invalido; isto nao substitui autenticacao.")
    return indices

def main():
    chave = os.urandom(16)
    dados = b"Mensagem de teste. " * 4
    print("Mensagem:", repr(dados), "|", len(dados), "bytes")
    for nome in ("ECB", "CBC", "CFB", "OFB"):
        experiencia(nome, dados, chave)

if __name__ == "__main__":
    main()
