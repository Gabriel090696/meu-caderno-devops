from fastapi.testclient import TestClient
from src.main import app, DOCS_PATH
import os

client = TestClient(app)

def test_listar_documentos():
    # 🔥 Garante que existe um arquivo .md para o teste
    os.makedirs(DOCS_PATH, exist_ok=True)

    caminho_arquivo = os.path.join(DOCS_PATH, "teste.md")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("# Teste")

    response = client.get("/")

    assert response.status_code == 200
    assert "teste.md" in response.text


def test_documento_inexistente():
    response = client.get("/doc/arquivo_que_nao_existe.md")

    assert response.status_code == 404
    assert response.json()["detail"] == "Arquivo não encontrado"do"