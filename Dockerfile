# Use a imagem base do Python
FROM python:3.11-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie requirements.txt e o src para o diretório de trabalho
COPY requirements.txt .
COPY /src .

# Copie o arquivo wait_for_host.sh com as permissões corretas
COPY wait_for_host.sh /tmp/wait_for_host.sh
RUN chmod +x /tmp/wait_for_host.sh

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Variáveis de ambiente para o Flask e o SQLAlchemy
ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta em que o servidor Flask estará em execução
EXPOSE 5000

# Comando para executar a aplicação
CMD flask run