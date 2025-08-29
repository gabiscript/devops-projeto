
# DevOps Fase 2 

## Descrição do Projeto

Este projeto visa implementar a segunda fase do projeto de DevOps, com foco na configuração de um pipeline de CI, containerização da aplicação Flask com Docker, push da imagem pro DockerHub e deploy automático na AWS EC2 via SSH.

## Requisitos

- Python 3.11
- Docker
- AWS Account com instância EC2 configurada
- Chave SSH para acessar a EC2
- Conta Github com as seguintes secrets configuradas: 
   - DOCKER_USERNAME
   - DOCKER_PASSWORD
   - EC2_HOST
   - EC2_KEY

## Instalação e Uso

1. Clone o repositório
   ```
   git clone https://github.com/gabiscript/devops-projeto.git
   cd devops-projeto
   ```
2. Instale as dependências Python
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Rode a aplicação (opcional)
   ```
   python app.py
   ```
4.  Rode os testes
   ```
   pytest
   ```
5. Criar infraestrutura AWS (apenas na primeira configuração da infraestrutura AWS)
    ```
    cd infra
    terraform init
    terraform validate
    terraform plan
    terraform apply
    ```
6. Containerizar e rodar com Docker
   ```
   docker build -t gabrielamds/devops-api:latest .
   docker run -d -p 5000:5000 --name devops-api gabrielamds/devops-api:latest
   ```
7. Deploy via Github Actions
   1. faça push para a branch main
   2. o workflow do Github Actions irá rodar os testes, buildar, enviar a imagem pro DockerHub, conectar na EC2 e atualizar o container
[![CI Fase 2 - Python + Docker + EC2](https://github.com/gabiscript/devops-projeto/actions/workflows/main.yml/badge.svg)](https://github.com/gabiscript/devops-projeto/actions/workflows/main.yml)

