"""Gera um BMP sintetico e cifra apenas os seus pixels (demonstracao)."""
import os
import struct
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def criar_bmp():
    largura, altura = 128, 128
    pixels = bytearray()
    # 128 * 3 bytes por linha: multiplo de 4 e de 16.
    for y in range(altura):
        for x in range(largura):
            cor = (220, 190, 30) if (x // 32 + y // 32) % 2 else (40, 40, 40)
            pixels.extend(cor)  # Ordem BGR no BMP.
    cabecalho = struct.pack("<2sIHHI", b"BM", 54 + len(pixels), 0, 0, 54)
    dib = struct.pack("<IiiHHIIiiII", 40, largura, altura, 1, 24,
                      0, len(pixels), 2835, 2835, 0, 0)
    return cabecalho + dib, bytes(pixels)

def main():
    destino = Path(__file__).resolve().parents[1] / "evidence" / "bmp"
    destino.mkdir(parents=True, exist_ok=True)
    cabecalho, pixels = criar_bmp()
    assert len(pixels) % 16 == 0
    (destino / "original.bmp").write_bytes(cabecalho + pixels)
    chave, iv = os.urandom(16), os.urandom(16)
    for nome, modo in (("ecb", modes.ECB()), ("cbc", modes.CBC(iv))):
        ctx = Cipher(algorithms.AES(chave), modo).encryptor()
        ct = ctx.update(pixels) + ctx.finalize()
        (destino / f"{nome}.bmp").write_bytes(cabecalho + ct)
    print("Imagens criadas em:", destino)
    print("Cabecalho preservado; pixels alinhados; sem padding.")

if __name__ == "__main__":
    main()
