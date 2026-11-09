MENSAGEM = "D VHJXUDQFD GRV GDGRV H HVVHQFLDO"

def decifrar_cesar(texto, chave):
    resultado = ""
    for letra in texto:
        if "A" <= letra <= "Z":
            resultado += chr((ord(letra) - 65 - chave) % 26 + 65)
        else:
            resultado += letra
    return resultado

def forca_bruta(texto):
    return [(k, decifrar_cesar(texto, k)) for k in range(26)]

if __name__ == "__main__":
    for chave, texto in forca_bruta(MENSAGEM):
        print(f"Chave {chave:02d}: {texto}")
    print("\nObservem os candidatos e identifiquem a mensagem legivel.")
