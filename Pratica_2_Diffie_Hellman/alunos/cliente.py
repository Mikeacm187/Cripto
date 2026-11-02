"""Alice: estabelece TCP, acorda K, envia texto público com HMAC e recebe resposta."""
from comum import *
def main():
    p=argumentos('Alice / cliente')
    p.add_argument('--mensagem',default='Reunião às 10h na sala de redes')
    p.add_argument('--p',type=int,default=P,help='Alterar apenas na experiência de erro')
    args=p.parse_args(); a=segredo(args.segredo); A=pow(G,a,P)
    c=Canal(socket.create_connection((args.host,args.porta),timeout=8))
    try:
        print('TCP local/remoto:',c.s.getsockname(),c.s.getpeername(),flush=True)
        c.envia({'tipo':'hello','p':args.p,'g':G,'A':A})
        B=publico(c.recebe('resposta'),'B'); k=pow(B,a,P); mostra(a,A,k)
        c.envia({'tipo':'dados','texto':args.mensagem,'mac':etiqueta(k,args.mensagem)})
        print('Resposta com MAC válido:',confere(k,c.recebe('dados')),flush=True)
    finally: c.fecha()
if __name__=='__main__': executar(main)
