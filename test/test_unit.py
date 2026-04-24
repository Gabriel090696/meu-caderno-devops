from src.main import (
    listar_arquivos_markdown,
    gerar_links_html,
    converter_markdown_para_html,
    ler_arquivo_markdown,
)

def test_gerar_links_html():
    arquivos = ["devops.md", "docker.md"]
    resultado = gerar_links_html(arquivos)

    assert '/doc/devops.md' in resultado
    assert '/doc/docker.md' in resultado
    assert '<li><a href="' in resultado
##dds
def test_converter_markdown_para_html():
    texto = "# Título"
    resultado = converter_markdown_para_html(texto)

    assert "<h1>" in resultado
    assert "Título" in resultado

def test_listar_arquivos_markdown(tmp_path):
    (tmp_path / "devops.md").write_text("# DevOps", encoding="utf-8")
    (tmp_path / "docker.md").write_text("# Docker", encoding="utf-8")
    (tmp_path / "imagem.png").write_text("binario", encoding="utf-8")

    resultado = listar_arquivos_markdown(tmp_path)

    assert "devops.md" in resultado
    assert "docker.md" in resultado
    assert "imagem.png" not in resultado


def test_ler_arquivo_markdown(tmp_path):
    arquivo = tmp_path / "teste.md"
    arquivo.write_text("# Conteúdo de teste", encoding="utf-8")

    resultado = ler_arquivo_markdown(arquivo)

    assert resultado == "# Conteúdo de teste"