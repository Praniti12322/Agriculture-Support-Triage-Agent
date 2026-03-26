variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = "string"
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = "string"
  default     = "t3.medium"
}

variable "key_name" {
  description = "Name of the existing AWS Key Pair"
  type        = "string"
  default     = "vignesh"
}

variable "ami_id" {
  description = "Ubuntu 22.04 AMI ID for ap-south-1"
  type        = "string"
  default     = "ami-03f4878755434977f" # Ubuntu 22.04 LTS in ap-south-1
}
