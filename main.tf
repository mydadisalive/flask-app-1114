provider "aws" {
  region = "us-east-1"  # Change to your preferred AWS region
}

resource "aws_instance" "web" {
  ami           = "ami-0df8c184d5f6ae949"  # Amazon Linux 2 AMI (Update based on region)
  instance_type = "t2.micro"
  key_name      = "my-key"  # Replace with your AWS key pair name

  security_groups = [aws_security_group.web_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Apache Server Running on $(hostname -f)!!!!</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "Terraform-Apache-Instance-tf"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "web-server-sg-tf"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow SSH from anywhere (Change for security)
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow HTTP from anywhere
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
