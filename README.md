# DevOps Fase 1 

## Descrição do Projeto

Este projeto visa implementar a primeira fase do projeto de DevOps, com foco na configuração de um pipeline de CI e automação inicial da infraestrutura.

## Requisitos

- Python 3.11
- Terraform
- AWS Account para criação de instancias EC2
- Chave SSH configurada para acessar o servidor

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
3. Rode a aplicação
   ```
   python app.py
   ```
4.  Rode os testes
   ```
   pytest
   ```
5. Crie a infraestrutura na AWS
   ```
   cd infra
   terraform init
   terraform validate
   terraform plan
   terraform apply
   
