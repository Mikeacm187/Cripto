import argparse
from cryptography.hazmat.primitives import padding

TAMANHO = 16

def blocos(dados):
    return [dados[i:i + TAMANHO] for i in range(0, len(dados), TAMANHO)]

def preencher(dados):
    n = TAMANHO - len(dados) % TAMANHO
    return dados + bytes([n]) * n

def remover_preenchimento(dados):
    if not dados or len(dados) % TAMANHO:
        raise ValueError("Comprimento invalido para PKCS#7.")
    n = dados[-1]
    if not 1 <= n <= TAMANHO or dados[-n:] != bytes([n]) * n:
        raise ValueError("Preenchimento PKCS#7 invalido.")
    return dados[:-n]

def mostrar(titulo, dados):
    print(f"\n{titulo}: {len(dados)} bytes")
    if not dados:
        print("Sem blocos.")
    for i, bloco in enumerate(blocos(dados), 1):
        print(f"Bloco {i}: {len(bloco)} bytes | {bloco!r} | {bloco.hex()}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mensagem", nargs="?")
    args = parser.parse_args()
    mensagem = args.mensagem
    if mensagem is None:
        mensagem = input("Introduza uma mensagem: ")
    dados = mensagem.encode("utf-8")
    print(f"Caracteres: {len(mensagem)}; bytes UTF-8: {len(dados)}")
    mostrar("Antes do preenchimento", dados)
    if not dados:
        print("Mensagem vazia: nao existe ultimo bloco.")
    else:
        print("Ultimo bloco completo:", len(dados) % TAMANHO == 0)
    preenchidos = preencher(dados)
    mostrar("Depois do preenchimento PKCS#7", preenchidos)
    print("Bytes acrescentados:", len(preenchidos) - len(dados))
    # Verificacao independente com a biblioteca.
    p = padding.PKCS7(128).padder()
    assert preenchidos == p.update(dados) + p.finalize()
    assert remover_preenchimento(preenchidos) == dados
    print("Remocao do preenchimento: OK")

if __name__ == "__main__":
    main()
