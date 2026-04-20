# 🐳 Docker no contexto de DevOps

## 📌 O que é Docker?

Docker é uma plataforma que permite criar, empacotar e executar aplicações em ambientes isolados chamados **containers**.

Diferente das máquinas virtuais, o Docker não precisa de um sistema operacional completo para cada aplicação. Ele utiliza o mesmo sistema base, tornando o processo mais leve, rápido e eficiente.

---

## ⚙️ Containers vs Máquinas Virtuais

### 🖥️ Máquinas Virtuais (VMs)
- Cada VM possui um sistema operacional completo
- Alto consumo de memória e processamento
- Inicialização mais lenta
- Isolamento total

### 🐳 Containers (Docker)
- Compartilham o mesmo sistema operacional
- Executam apenas o necessário para a aplicação
- Inicialização rápida
- Menor consumo de recursos
- Maior eficiência

---

## 🚀 Vantagens do Docker

- Portabilidade: roda em qualquer ambiente
- Consistência: evita problemas como "funciona na minha máquina"
- Rapidez na execução
- Facilidade de escalabilidade
- Ideal para integração com pipelines de CI/CD

---

## 🔄 Uso do Docker no DevOps

Docker é amplamente utilizado em práticas de DevOps, principalmente em:

### 🔹 CI/CD
Permite criar ambientes padronizados para:
- build da aplicação
- execução de testes
- validação de código
- deploy automatizado

### 🔹 Microsserviços
Cada serviço pode rodar em um container independente:
- API
- banco de dados
- autenticação
- cache

Isso facilita:
- manutenção
- escalabilidade
- desenvolvimento em equipe

### 🔹 Ambientes (Dev, Staging e Produção)

Docker garante que a aplicação funcione da mesma forma em todos os ambientes:

- **Desenvolvimento:** testes locais
- **Staging:** simulação do ambiente real
- **Produção:** sistema final para usuários

---

## 📦 Docker Hub

O Docker Hub é um repositório de imagens Docker.

Funciona como uma "loja" de containers, onde é possível:

- baixar imagens prontas
- compartilhar aplicações

### Exemplo de uso:

```bash
docker pull nginx
docker push minha-imagem