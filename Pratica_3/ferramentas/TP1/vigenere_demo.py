"""Interface de consola para as funções Vigenère fornecidas no TP1."""
from vigenereCipher import encryptMessage, decryptMessage

def main():
    print('Vigenère — experiência do TP1 (sem editar código)')
    while True:
        modo = input('1: cifrar | 2: decifrar | 0: sair > ').strip()
        if modo == '0':
            return
        if modo not in ('1', '2'):
            print('Escolhe 1, 2 ou 0.')
            continue
        chave = input('Chave (apenas letras A-Z, sem acentos): ').strip().upper()
        if not chave or any(letra not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for letra in chave):
            print('A chave tem de conter apenas letras A-Z.')
            continue
        mensagem = input('Mensagem: ')
        funcao = encryptMessage if modo == '1' else decryptMessage
        print('Resultado:', funcao(chave, mensagem))

if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print('\nExperiência terminada.')
