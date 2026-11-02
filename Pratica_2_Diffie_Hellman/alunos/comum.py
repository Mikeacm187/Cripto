"""Protocolo didático: JSON UTF-8, uma mensagem por linha, máximo 4096 bytes.
Não é um protocolo de segurança para utilização real.
"""
import argparse, socket, json, secrets, hashlib, hmac, sys
P, G = 23, 5
class Canal:
    def __init__(self,s):
        self.s=s
        s.settimeout(12)
        self.f=s.makefile('rb')
    def envia(self,obj):
        raw=json.dumps(obj,ensure_ascii=False,separators=(',',':')).encode()+b'\n'
        if len(raw)>4096: raise ValueError('Mensagem demasiado longa')
        self.s.sendall(raw)
        print('TX público:',raw.decode().strip(),flush=True)
    def recebe(self,tipo):
        raw=self.f.readline(4097)
        if not raw: raise ValueError('Ligação encerrada antes da mensagem esperada')
        if len(raw)>4096 or not raw.endswith(b'\n'): raise ValueError('Linha inválida ou demasiado longa')
        obj=json.loads(raw)
        if not isinstance(obj,dict) or obj.get('tipo')!=tipo: raise ValueError('Mensagem fora de ordem: esperado '+tipo)
        print('RX público:',raw.decode().strip(),flush=True)
        return obj
    def fecha(self):
        self.f.close(); self.s.close()
def inteiro(obj,nome):
    v=obj.get(nome)
    if type(v) is not int: raise ValueError('Campo inteiro inválido: '+nome)
    return v
def publico(obj,nome):
    v=inteiro(obj,nome)
    if not 2<=v<=P-2: raise ValueError('Valor público fora do intervalo didático')
    return v
def segredo(fixo):
    if fixo is None: return secrets.randbelow(8)+2
    if not 2<=fixo<=9: raise ValueError('O segredo didático deve estar entre 2 e 9')
    return fixo
def chave(k): return hashlib.sha256(str(k).encode()).digest()
def etiqueta(k,texto): return hmac.new(chave(k),texto.encode(),hashlib.sha256).hexdigest()
def confere(k,obj):
    texto=obj.get('texto'); tag=obj.get('mac')
    if not isinstance(texto,str) or not isinstance(tag,str): raise ValueError('Texto/MAC inválido')
    if not hmac.compare_digest(etiqueta(k,texto),tag): raise ValueError('MAC inválido: conteúdo ou segredo diferente')
    return texto
def mostra(priv,pub,k):
    print(f'LOCAL APENAS: privado={priv}; público={pub}; K={k}',flush=True)
def executar(fn):
    try: fn()
    except (OSError,ValueError,KeyError,TypeError,UnicodeError) as e:
        print(f'ERRO: {e}\nVer guia: endereço, porta, serviço, firewall ou protocolo.',file=sys.stderr)
        sys.exit(1)
def argumentos(papel):
    p=argparse.ArgumentParser(description='Laboratório DH inseguro e didático - '+papel)
    p.add_argument('--host',default='127.0.0.1')
    p.add_argument('--porta',type=int,default=5000)
    p.add_argument('--segredo',type=int)
    return p
