"""Mallory: proxy explícito de laboratório, sem ARP spoofing ou redirecionamento.
Cliente liga voluntariamente à porta 6000; Bob recebe uma segunda ligação TCP.
"""
from comum import *
def main():
    p=argumentos('Mallory / proxy explícito')
    p.set_defaults(porta=6000)
    p.add_argument('--destino',default='127.0.0.1')
    p.add_argument('--porta-servidor',type=int,default=5000)
    p.add_argument('--alterar',action='store_true')
    args=p.parse_args()
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((args.host,args.porta)); s.listen(1); s.settimeout(120)
        print('Mallory à escuta:',s.getsockname(),flush=True)
        conn,_=s.accept(); alice=Canal(conn); bob=None
        try:
            h=alice.recebe('hello')
            if inteiro(h,'p')!=P or inteiro(h,'g')!=G: raise ValueError('Parâmetros incompatíveis')
            A=publico(h,'A')
            # Dois privados de Mallory: 3 para Alice e 4 para Bob.
            ma,mb=3,4
            bob=Canal(socket.create_connection((args.destino,args.porta_servidor),timeout=8))
            bob.envia({'tipo':'hello','p':P,'g':G,'A':pow(G,mb,P)})
            B=publico(bob.recebe('resposta'),'B')
            alice.envia({'tipo':'resposta','B':pow(G,ma,P)})
            ka,kb=pow(A,ma,P),pow(B,mb,P)
            print(f'LOCAL Mallory: K com Alice={ka}; K com Bob={kb}',flush=True)
            texto=confere(ka,alice.recebe('dados')); print('Mallory leu:',texto,flush=True)
            if args.alterar: texto='Reunião alterada para as 15h por Mallory'
            bob.envia({'tipo':'dados','texto':texto,'mac':etiqueta(kb,texto)})
            resposta=confere(kb,bob.recebe('dados'))
            alice.envia({'tipo':'dados','texto':resposta,'mac':etiqueta(ka,resposta)})
        finally:
            alice.fecha()
            if bob: bob.fecha()
if __name__=='__main__': executar(main)
