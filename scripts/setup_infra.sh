#!/bin/bash

# Automation script to install Terraform and provision infrastructure

set -e

echo "🚀 Starting Infrastructure Setup..."

# 1. Install Terraform (if not present)
if ! command -v terraform &> /dev/null; then
    echo "📦 Installing Terraform..."
    sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
    curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt-get update && sudo apt-get install terraform
else
    echo "✅ Terraform is already installed."
fi

# 2. Initialize and Provision
cd terraform
echo "🏗️ Initializing Terraform..."
terraform init

echo "📋 Planning Infrastructure..."
terraform plan -out=tfplan

echo "🚀 Applying Infrastructure..."
# terraform apply tfplan  # Commented out for safety; user should run manually
echo "DONE! Review the plan and run 'terraform apply tfplan' to provision resources."
