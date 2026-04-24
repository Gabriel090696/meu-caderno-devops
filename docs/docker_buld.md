Build da imagem
docker build -t meu-caderno-devops .

Rodar o container
docker run -p 8000:8000 meu-caderno-devops

http://localhost:8000