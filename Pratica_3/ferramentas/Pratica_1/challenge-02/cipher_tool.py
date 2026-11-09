def transformar(texto, chave):
    resultado = ""
    for letra in texto:
        if "A" <= letra <= "Z":
            base = ord("A")
        elif "a" <= letra <= "z":
            base = ord("a")
        else:
            resultado += letra
            continue
        resultado += chr((ord(letra) - base + chave) % 26 + base)
    return resultado

def ler_chave():
    while True:
        try:
            return int(input("Chave inteira: ")) % 26
        except ValueError:
            print("Entrada invalida: introduza um numero inteiro.")

def main():
    while True:
        print("\n[1] Cifrar mensagem\n[2] Decifrar mensagem")
        print("[3] Ataque por forca bruta\n[4] Sair")
        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "4":
            print("Ate breve!")
            break
        if opcao not in {"1", "2", "3"}:
            print("Opcao invalida.")
            continue
        texto = input("Mensagem: ")
        if opcao == "3":
            for k in range(26):
                print(f"{k:02d}: {transformar(texto, -k)}")
        else:
            chave = ler_chave()
            deslocamento = chave if opcao == "1" else -chave
            print("Resultado:", transformar(texto, deslocamento))

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nAplicacao terminada.")
