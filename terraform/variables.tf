variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "c7i-flex.large"
}

variable "key_name" {
  description = "Name of the existing AWS Key Pair"
  type        = string
  default     = "krishi-key"
}

variable "ami_id" {
  description = "Ubuntu 24.04 AMI ID for ap-south-1"
  type        = string
  default     = "ami-0a14f53a6fe4dfcd1" 
}
