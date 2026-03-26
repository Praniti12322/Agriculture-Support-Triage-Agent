output "public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.agriculture_server.public_ip
}

output "ssh_command" {
  description = "SSH command to access the server"
  value       = "ssh -i ${var.key_name}.pem ubuntu@${aws_instance.agriculture_server.public_ip}"
}
