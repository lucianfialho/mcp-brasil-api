FROM python:3.13-slim

WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app/

# Instalar dependências
RUN pip install --no-cache-dir httpx>=0.28.1 mcp[cli]>=1.4.1 python-dotenv>=1.0.1

# O comando será fornecido pelo smithery.yaml
CMD ["python", "server.py"]