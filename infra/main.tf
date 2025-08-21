provider "aws" {
  region = "us-east-1" 
}

resource "aws_instance" "devops_server" {
  ami           = "ami-0c02fb55956c7d316" 
  instance_type = "t3.micro"
  key_name      = "devops-key"

  tags = {
    Name = "Servidor-DevOps-Fase1"
  }
}

output "public_ip" {
  value = aws_instance.devops_server.public_ip
}

output "instance_id" {
  value = aws_instance.devops_server.id
}
