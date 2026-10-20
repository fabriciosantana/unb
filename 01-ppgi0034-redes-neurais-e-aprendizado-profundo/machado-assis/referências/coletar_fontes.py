"""Baixa fontes públicas selecionadas; preserva metadados e hashes, sem APIs bibliográficas."""
import concurrent.futures, hashlib, io, json, re
from html.parser import HTMLParser
from pathlib import Path
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
class Meta(HTMLParser):
    def __init__(self):
        super().__init__(); self.values = {}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('name', '').startswith('citation_'):
            self.values.setdefault(a['name'], []).append(a.get('content', ''))

ARXIV = [
 ('vaswani2017','1706.03762','essencial','Transformer e atenção'),
 ('brown2020','2005.14165','enunciado','GPT-3 e aprendizado em contexto'),
 ('ba2016','1607.06450','apoio','Layer normalization'),
 ('kingma2014','1412.6980','apoio','Adam'),
 ('loshchilov2017','1711.05101','essencial','AdamW'),
 ('hendrycks2016','1606.08415','apoio','GELU'),
 ('holtzman2019','1904.09751','essencial','Decodificação e nucleus sampling'),
 ('kaplan2020','2001.08361','avançado','Escala de modelos'),
 ('hoffmann2022','2203.15556','avançado','Orçamento de computação e dados'),
 ('lewis2020rag','2005.11401','extensão','RAG e perguntas e respostas'),
 ('hu2021','2106.09685','extensão','LoRA'),
 ('ouyang2022','2203.02155','extensão','Instruction tuning e RLHF'),
 ('zhao2023','2303.18223','panorama','Revisão ampla de LLMs'),
]
ACL = [
 ('sennrich2016','P16-1162','essencial','BPE'),
 ('kudo2018','D18-2012','apoio','SentencePiece'),
 ('lee2022','2022.acl-long.577','essencial','Deduplicação e contaminação'),
 ('gururangan2020','2020.acl-main.740','extensão','Adaptação de domínio'),
]
EXTRA = [
 dict(key='radford2019',url='https://cdn.openai.com/better-language-models/language-models.pdf',pdf_url='https://cdn.openai.com/better-language-models/language-models.pdf',title='Language Models are Unsupervised Multitask Learners',authors=['Alec Radford','Jeffrey Wu','Rewon Child','David Luan','Dario Amodei','Ilya Sutskever'],year='2019',kind='techreport',institution='OpenAI',priority='essencial',topic='GPT-2'),
 dict(key='srivastava2014',url='https://jmlr.org/papers/v15/srivastava14a.html',pdf_url='https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf',title='Dropout: A Simple Way to Prevent Neural Networks from Overfitting',authors=['Nitish Srivastava','Geoffrey Hinton','Alex Krizhevsky','Ilya Sutskever','Ruslan Salakhutdinov'],year='2014',kind='article',journal='Journal of Machine Learning Research',volume='15',pages='1929--1958',priority='apoio',topic='Regularização'),
 dict(key='jurafsky2026',url='https://web.stanford.edu/~jurafsky/slp3/',pdf_url='https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf',title='Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition, with Language Models',authors=['Daniel Jurafsky','James H. Martin'],year='2026',kind='book',edition='3',note='Manuscrito online, versão de 19 de agosto de 2026',priority='essencial',topic='Livro-base de PLN'),
 dict(key='zhang2023',url='https://d2l.ai/',pdf_url='https://d2l.ai/d2l-en.pdf',title='Dive into Deep Learning',authors=['Aston Zhang','Zachary C. Lipton','Mu Li','Alexander J. Smola'],year='2023',kind='book',publisher='Cambridge University Press',priority='essencial',topic='Matemática, redes neurais e implementação'),
 dict(key='ufu2025',url='https://bibliotecas.ufu.br/en/node/3660',pdf_url='https://bibliotecas.ufu.br/sites/bibliotecas.ufu.br/files/media/imagem/referencias_maio_2025_2.pdf',title='Elaboração de referências: ABNT NBR 6023/2025',authors=['{Universidade Federal de Uberlândia. Sistema de Bibliotecas}'],year='2025',kind='misc',priority='consulta',topic='Formatação de referências'),
]

def collect(item):
    d = dict(item); key=d['key']
    try:
        if d.get('source') in ('arxiv','acl'):
            r=requests.get(d['url'],timeout=60); r.raise_for_status()
            parser=Meta(); parser.feed(r.text); m=parser.values
            (ROOT/'metadados').mkdir(exist_ok=True)
            (ROOT/'metadados'/f'{key}.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
            d.update(title=m['citation_title'][0],authors=m['citation_author'],year=m.get('citation_publication_date',m.get('citation_date',['']))[0][:4])
            d['kind']='misc' if d['source']=='arxiv' else 'inproceedings'
            for source,target in [('citation_doi','doi'),('citation_conference_title','booktitle'),('citation_publisher','publisher')]:
                if m.get(source): d[target]=m[source][0]
            if d['source']=='arxiv':
                d['doi']='10.48550/arXiv.'+d['id']; d['eprint']=d['id']; d['note']='Versão arXiv; ano da submissão inicial'
                versions=re.findall(r'/abs/'+re.escape(d['id'])+r'v(\d+)',r.text)
                d['version']='v'+str(max(map(int,versions))) if versions else 'não identificada'
            else:
                if m.get('citation_firstpage') and m.get('citation_lastpage'): d['pages']=m['citation_firstpage'][0]+'--'+m['citation_lastpage'][0]
        if d.get('pdf_url'):
            out=ROOT/f'{key}.pdf'
            if out.exists(): data=out.read_bytes()
            else:
                r=requests.get(d['pdf_url'],timeout=150); r.raise_for_status(); data=r.content
            if not data.startswith(b'%PDF-'): raise ValueError('Resposta não é PDF')
            reader=PdfReader(io.BytesIO(data),strict=True)
            d.update(pages_pdf=len(reader.pages),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),pdf_status='baixado e parseado',file=out.name)
            out.write_bytes(data)
            excerpts='\n'.join(p.extract_text() or '' for p in reader.pages[:2])
            (ROOT/'metadados'/f'{key}-inicio.txt').write_text(excerpts)
        d['access_date']='2026-09-25'
    except Exception as e: d['error']=str(e); d.setdefault('pdf_status','falhou')
    print(key,d.get('pdf_status'),d.get('error',''),flush=True)
    return d

def main():
    items=[]
    for key,ident,priority,topic in ARXIV:
        items.append(dict(key=key,id=ident,url=f'https://arxiv.org/abs/{ident}',pdf_url=f'https://arxiv.org/pdf/{ident}',priority=priority,topic=topic,source='arxiv'))
    for key,ident,priority,topic in ACL:
        items.append(dict(key=key,id=ident,url=f'https://aclanthology.org/{ident}/',pdf_url=f'https://aclanthology.org/{ident}.pdf',priority=priority,topic=topic,source='acl'))
    (ROOT/'metadados').mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(collect,items+EXTRA))
    (ROOT/'fontes.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
