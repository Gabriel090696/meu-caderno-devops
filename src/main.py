from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os
import markdown

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_PATH = os.path.join(BASE_DIR, "docs")


def listar_arquivos_markdown(caminho_docs):
    return [f for f in os.listdir(caminho_docs) if f.endswith(".md")]


def gerar_links_html(arquivos):
    return "".join([f'<li><a href="/doc/{f}">{f}</a></li>' for f in arquivos])


def ler_arquivo_markdown(caminho_completo):
    with open(caminho_completo, "r", encoding="utf-8") as file:
        return file.read()


def converter_markdown_para_html(texto_markdown):
    return markdown.markdown(texto_markdown)


@app.get("/", response_class=HTMLResponse)
def listar_documentos():
    arquivos = listar_arquivos_markdown(DOCS_PATH)
    links = gerar_links_html(arquivos)

    html_content = f"""
    <html>
        <head><title>  Caderno DevOps</title></head>
        <body>
            <h1>Docs do Projeto Meu Caderno Minha Vida</h1>
            <ul>{links}</ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/doc/{arquivo_nome}", response_class=HTMLResponse)
def ler_documento(arquivo_nome: str):
    caminho_completo = os.path.join(DOCS_PATH, arquivo_nome)

    if os.path.exists(caminho_completo):
        texto_markdown = ler_arquivo_markdown(caminho_completo)
        html_convertido = converter_markdown_para_html(texto_markdown)

        return HTMLResponse(content=f"""
            <html>
                <head>
                    <style>
                        body {{ font-family: sans-serif; padding: 40px; line-height: 1.6; color: #333; }}
                        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
                    </style>
                </head>
                <body>
                    <a href="/">← Voltar</a>
                    {html_convertido}
                </body>
            </html>
        """)

    raise HTTPException(status_code=404, detail="Arquivo não encontrado")