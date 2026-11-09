import socket
import threading
import sys

# Cifra → texto original
mapping = {
    "A": "Y", "B": "M", "C": "N", "F": "V",
    "G": "T", "H": "I", "I": "O", "J": "P",
    "K": "G", "L": "D", "M": "C", "N": "B",
    "O": "L", "P": "K", "Q": "H", "R": "U",
    "S": "W", "T": "R", "U": "A", "V": "S",
    "X": "E", "Y": "Q", "Z": "F",
    "D": "J", "E": "X", "W": "Z"
}

cifrar = str.maketrans({v: k for k, v in mapping.items()})
decifrar = str.maketrans(mapping)
PORTA = 5001

clientes = set()
lock = threading.Lock()


def atender(cliente):
    try:
        with cliente.makefile("rb") as entrada:
            for mensagem in entrada:
                cifra_recebida = mensagem.decode("utf-8", errors="replace").rstrip("\n")
                print(f"\n[SERVIDOR] Recebido de {cliente.getpeername()}: {cifra_recebida}", flush=True)
                # Uma mensagem por linha; encaminhar sem decifrar.
                with lock:
                    for outro in list(clientes):
                        if outro is not cliente:
                            try:
                                outro.sendall(mensagem)
                                print(f"[SERVIDOR] Encaminhado para {outro.getpeername()}: {cifra_recebida}", flush=True)
                            except OSError:
                                clientes.discard(outro)
                                outro.close()
    except OSError:
        pass
    finally:
        with lock:
            clientes.discard(cliente)
        cliente.close()


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", PORTA))
        sock.listen()
        print(f"Servidor à escuta na porta {PORTA}")

        while True:
            cliente, endereco = sock.accept()
            print(f"Ligação: {endereco}")
            with lock:
                clientes.add(cliente)
            threading.Thread(
                target=atender, args=(cliente,), daemon=True
            ).start()


def receber(sock):
    try:
        with sock.makefile("rb") as entrada:
            for mensagem in entrada:
                texto = mensagem.decode("utf-8").rstrip("\n")
                print(f"\n[RECEÇÃO] Cifra recebida: {texto}", flush=True)
                print(f"[DECIFRAÇÃO] {texto} → {texto.translate(decifrar)}", flush=True)
    except (OSError, UnicodeError):
        pass
    print("\nLigação ao servidor terminada.")


def cliente(host):
    nome = input("Nome: ").strip()

    with socket.create_connection((host, PORTA)) as sock:
        threading.Thread(
            target=receber, args=(sock,), daemon=True
        ).start()
        print("Escreve mensagens. Usa /sair para terminar.")

        try:
            while True:
                texto = input()
                if texto == "/sair":
                    break

                original = f"{nome}: {texto}".upper()
                mensagem = original.translate(cifrar)
                print(f"[CIFRAÇÃO] {original} → {mensagem}", flush=True)
                print(f"[ENVIO] Cifra enviada ao servidor: {mensagem}", flush=True)
                sock.sendall((mensagem + "\n").encode("utf-8"))
        except (EOFError, KeyboardInterrupt, OSError):
            pass
        finally:
            sock.shutdown(socket.SHUT_RDWR)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 chat.py servidor|cliente [IP]")
    elif sys.argv[1] == "servidor":
        servidor()
    elif sys.argv[1] == "cliente":
        host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        cliente(host)
    else:
        print("Modo inválido: usa servidor ou cliente.")