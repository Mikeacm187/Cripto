"""Bob: aceita uma sessão e termina. Reiniciar para cada experiência."""
from comum import *
import time

def main():
    p=argumentos('Bob / servidor')
    p.add_argument('--atraso',type=float,default=0,help='Atraso antes de responder, em segundos')
    args=p.parse_args(); b=segredo(args.segredo); B=pow(G,b,P)
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((args.host,args.porta)); s.listen(1); s.settimeout(120)
        print(f'Bob à escuta em {args.host}:{args.porta}',flush=True)
        conn,peer=s.accept(); print('Cliente:',peer,flush=True); c=Canal(conn)
        try:
            hello=c.recebe('hello')
            if inteiro(hello,'p')!=P or inteiro(hello,'g')!=G: raise ValueError('Parâmetros p/g incompatíveis')
            A=publico(hello,'A'); time.sleep(max(0,args.atraso))
            c.envia({'tipo':'resposta','B':B}); k=pow(A,b,P); mostra(b,B,k)
            texto=confere(k,c.recebe('dados')); print('Texto recebido e MAC válido:',texto,flush=True)
            resposta='Bob recebeu: '+texto
            c.envia({'tipo':'dados','texto':resposta,'mac':etiqueta(k,resposta)})
        finally: c.fecha()
if __name__=='__main__': executar(main)
