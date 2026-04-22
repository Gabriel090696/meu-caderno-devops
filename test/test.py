from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_listar_documentos():
    response = client.get("/")
    assert response.status_code == 200
    assert "Docs do ProjetoMeu Caderno Minha Vida" in response.text

def test_documento_inexistente():
    response = client.get("/doc/arquivo_que_nao_existe.md")
    assert response.status_code == 404
    assert response.json()["detail"] == "Arquivo não encontrado"