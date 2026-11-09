"""Mostra por que p=23 NÃO protege nada. Usar A/B observados no Wireshark."""
from comum import *
def main():
    p=argparse.ArgumentParser(); p.add_argument('--A',type=int,required=True); p.add_argument('--B',type=int,required=True)
    v=p.parse_args(); publico({'A':v.A},'A'); publico({'B':v.B},'B')
    for candidato in range(1,P-1):
        if pow(G,candidato,P)==v.A:
            print('Expoente compatível:',candidato,'; K recuperado:',pow(v.B,candidato,P)); return
    raise ValueError('Sem expoente compatível')
if __name__=='__main__': executar(main)
