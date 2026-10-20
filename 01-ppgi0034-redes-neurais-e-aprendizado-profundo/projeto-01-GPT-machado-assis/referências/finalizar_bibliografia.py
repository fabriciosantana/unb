"""Gera BibTeX, lista ABNT e inventário a partir das fontes conferidas."""
import hashlib, io, json, re, subprocess, sys
from pathlib import Path
import requests
from pypdf import PdfReader
import bibtexparser
ROOT=Path(__file__).resolve().parent
PREFLIGHT=Path('/home/vscode/.codex/plugins/cache/ars-codex/ars-codex/3.22.0/skills/academic-research-suite/ars/scripts/pdf_read_preflight.py')

def main():
    sources=[d for d in json.loads((ROOT/'fontes.json').read_text()) if d.get('pdf_url')]
    d=next(d for d in sources if d['key']=='jurafsky2026')
    if not (ROOT/'jurafsky2026.pdf').exists():
        r=requests.get(d['pdf_url'],timeout=180); r.raise_for_status()
        assert r.content.startswith(b'%PDF-')
        (ROOT/'jurafsky2026.pdf').write_bytes(r.content)
    data=(ROOT/'jurafsky2026.pdf').read_bytes()
    reader=PdfReader(io.BytesIO(data),strict=False)
    d.update(file='jurafsky2026.pdf',pdf_status='baixado; parser estrito emitiu erro; leitura tolerante disponível',pages_pdf=len(reader.pages),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),access_date='2026-09-25')
    # Fontes online sem PDF editorial; não produzir PDFs artificiais.
    extra=[
      ('goodfellow2016',['Ian Goodfellow','Yoshua Bengio','Aaron Courville'],'Deep Learning','2016','https://www.deeplearningbook.org/','book','Fundamentos adicionais','HTML gratuito; autores não disponibilizam PDF'),
      ('karpathyNanoGPT',['Andrej Karpathy'],'nanoGPT',None,'https://github.com/karpathy/nanoGPT','misc','Código-base exigido','Repositório; registrar commit usado no experimento'),
      ('karpathyTutorial',['Andrej Karpathy'],"Let’s build GPT: from scratch, in code, spelled out.",None,'https://www.youtube.com/watch?v=kCc8FmEb1nY','misc','Tutorial exigido','Vídeo; data não confirmada na consulta'),
      ('mecMachado',['{Brasil. Ministério da Educação}','{Universidade Federal de Santa Catarina. NUPILL}'],'Machado de Assis: vida e obra',None,'https://machado.mec.gov.br/','misc','Proveniência do corpus','Portal da coleção digital; citar também cada edição efetivamente usada'),
      ('abl2020',['{Academia Brasileira de Letras}'],'Machado de Assis gratuito','2020','https://www.academia.org.br/boletins/machado-de-assis-gratuito','misc','Contexto da coleção','Publicado em 18 de junho de 2020'),
      ('ieeeTemplates',['{IEEE}'],'Authoring tools and templates',None,'https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/','misc','Formato do artigo','Página oficial dos modelos de conferência'),
      ('abnt2025',['{Associação Brasileira de Normas Técnicas}'],'ABNT NBR 6023: informação e documentação: referências: elaboração','2025','https://www.dinmedia.de/en/standard/abnt-nbr-6023/393096544','manual','Norma de referências','3ª edição; norma integral não baixada; catálogo bibliográfico'),
    ]
    for key,authors,title,year,url,kind,topic,note in extra:
        sources.append(dict(key=key,authors=authors,title=title,year=year,url=url,kind=kind,topic=topic,note=note,priority='consulta',pdf_status='fonte sem PDF baixável selecionado',access_date='2026-09-25'))
    next(d for d in sources if d['key']=='goodfellow2016').update(publisher='MIT Press',address='Cambridge, MA')
    next(d for d in sources if d['key']=='ufu2025').update(publisher='UFU',address='Uberlândia')
    next(d for d in sources if d['key']=='abl2020').update(publisher='Academia Brasileira de Letras',address='Rio de Janeiro')
    next(d for d in sources if d['key']=='mecMachado').update(publisher='Ministério da Educação')
    next(d for d in sources if d['key']=='ieeeTemplates').update(publisher='IEEE')
    next(d for d in sources if d['key']=='zhang2023').update(address='Cambridge',note='Edição publicada em 2023; PDF online evolutivo, snapshot de 25 set. 2026')
    next(d for d in sources if d['key']=='abnt2025').update(organization='Associação Brasileira de Normas Técnicas',address='Rio de Janeiro',edition='3')
    # Metadados ACL: completar local dos anais a partir do BibTeX oficial.
    for d in sources:
        if d.get('source')=='acl':
            r=requests.get(d['url'].rstrip('/')+'.bib',timeout=60); r.raise_for_status()
            (ROOT/'metadados'/f"{d['key']}-oficial.bib").write_text(r.text)
            lib=bibtexparser.parse_string(r.text)
            e=lib.entries[0]
            for f in ['address','publisher','pages','booktitle','doi']:
                if e.get(f): d[f]=e[f]
        if d.get('source')=='arxiv':
            d['note']='Versão arXiv; ano da submissão inicial; PDF '+d['version']+' consultado em 25 set. 2026'
    # Verificação estrutural ARS é distinta da inspeção temática.
    for d in sources:
        if d.get('file'):
            side=ROOT/'metadados'/f"{d['key']}-estrutura.json"
            subprocess.run([sys.executable,str(PREFLIGHT),str(ROOT/d['file']),'--output',str(side)],check=True,stdout=subprocess.DEVNULL)
            obj=json.loads(side.read_text()); d['structural_verdict']=obj.get('verdict','consultar sidecar')
    (ROOT/'fontes.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2))
    fields=['title','year','publisher','address','institution','journal','volume','pages','booktitle','edition','organization','doi','eprint','note']
    bib=['% Biblioteca de estudo: Projeto Machado de Assis. Consulta: 2026-09-25.','% Entradas arXiv citam a submissão inicial e identificam a versão consultada.']
    for d in sources:
        vals={'author':' and '.join(d['authors'])}
        vals.update({f:str(d[f]) for f in fields if d.get(f)})
        vals['title']='{'+vals['title']+'}'
        vals.update(url=d['url'],urldate='2026-09-25')
        if d.get('eprint'): vals['archivePrefix']='arXiv'
        if d.get('file'): vals['file']=d['file']
        if not d.get('year'): vals['note']=vals.get('note','')+'; data de publicação não identificada'
        bib.append('@'+d['kind']+'{'+d['key']+',\n'+',\n'.join('  '+k+' = {'+v.replace('&',r'\&').replace('%',r'\%')+'}' for k,v in vals.items())+'\n}')
    bibtext='\n\n'.join(bib)+'\n'
    library=bibtexparser.parse_string(bibtext)
    assert len(library.entries)==len(sources) and not library.failed_blocks
    (ROOT/'bibliografia.bib').write_text(bibtext)
    def person(a):
        if a.startswith('{'): return a.strip('{}').upper()
        if ',' in a: last,first=a.split(',',1)
        else: first,last=a.rsplit(' ',1)
        return last.upper()+', '+first.strip()
    def authors(d):
        a=d['authors']
        return person(a[0])+' et al.' if len(a)>3 else '; '.join(person(x) for x in a)
    out=['# Bibliografia em formato ABNT','Referências organizadas alfabeticamente, conforme NBR 6023:2025. Para quatro ou mais autores, adota-se primeiro autor e “et al.”; o BibTeX preserva todos. [S. l.] e [s. n.] indicam local/editora não identificados; [s. d.] indica data não identificada. As chaves entre colchetes são auxiliares para localizar o PDF e não fazem parte da referência. Entradas arXiv referenciam o depósito, sem inventar dados dos anais.\n']
    for d in sorted(sources,key=authors):
        base=authors(d).rstrip('.')+'. '
        year=d.get('year') or '[s. d.]'
        if d.get('source')=='acl':
            base+=d['title']+'. In: **'+d['booktitle']+'**. '+d.get('address','[S. l.]')+': '+d.get('publisher','Association for Computational Linguistics')+', '+year+'.'
            if d.get('pages'): base+=' p. '+d['pages'].replace('--','–')+'.'
        elif d['kind']=='article':
            base+=d['title']+'. **'+d['journal']+'**, [S. l.], v. '+d['volume']+', p. '+d['pages'].replace('--','–')+', '+year+'.'
        elif d.get('source')=='arxiv':
            base+='**'+d['title']+'**. [S. l.]: arXiv, '+year+'. arXiv:'+d['id']+'. Versão consultada: '+d['version']+'.'
        else:
            base+='**'+d['title'].rstrip('.')+'**. '
            if d.get('edition'): base+=d['edition']+'. ed. '
            base+=d.get('address','[S. l.]')+': '+d.get('publisher',d.get('institution',d.get('organization','[s. n.]')))+', '+year+'.'
            if d['key']=='jurafsky2026': base+=' Manuscrito online de 19 ago. 2026.'
        if d.get('doi'): base+=' DOI: '+d['doi']+'.'
        base+=' Disponível em: '+d['url']+'. Acesso em: 25 set. 2026.'
        out+=['## ['+d['key']+']',base,'']
    (ROOT/'bibliografia-abnt.md').write_text('\n\n'.join(out))
    inventory=['# Inventário de fontes e PDFs','Cada hash identifica os bytes baixados. PASS diz respeito somente à estrutura do PDF, não à validade científica. Não foi atestada leitura humana.\n','| Chave | Tema | Prioridade | PDF / situação | Estrutura |','|---|---|---|---|---|']
    for d in sources:
        link=f"[{d['file']}]({d['file']})" if d.get('file') else d['pdf_status']
        inventory.append(f"| `{d['key']}` | {d['topic']} | {d['priority']} | {link} | {d.get('structural_verdict','não se aplica')} |")
    inventory+=['','Metadados completos, URLs dos downloads, tamanho e SHA-256: [fontes.json](fontes.json).','O PDF de Jurafsky e Martin teve erro de dicionário duplicado no parser estrito. Foi preservado sem alteração e aberto em modo tolerante; consultar o sidecar estrutural. As referências ao livro usam capítulos, não páginas extraídas.','O livro Deep Learning é oferecido oficialmente em HTML, sem PDF autorizado no site. Repositório, vídeo, portais e norma também permanecem com links; não foram substituídos por arquivos HTML renomeados como PDF.']
    (ROOT/'inventario.md').write_text('\n'.join(inventory)+'\n')
    print('Entradas:',len(sources),'PDFs:',sum(bool(d.get('file')) for d in sources),'BibTeX: válido')

if __name__=='__main__': main()
