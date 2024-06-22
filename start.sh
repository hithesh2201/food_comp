#!/bin/bash

# Check if script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root."
    exit 1
fi

# Install Docker
echo "Installing Docker..."
yum-config-manager -y --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce -y
if [ $? -ne 0 ]; then
    echo "Error: Docker installation failed."
    exit 1
fi

# Start Docker service
echo "Starting Docker service..."
systemctl start docker
if [ $? -ne 0 ]; then
    echo "Error: Failed to start Docker service."
    exit 1
fi

# Clone the GitHub repository
echo "Cloning the GitHub repository..."
git clone https://github.com/hithesh2201/food_comp.git
if [ $? -ne 0 ]; then
    echo "Error: Unable to clone the repository."
    exit 1
fi

# Change directory to the project directory
cd food_comp || exit

# Build the Docker image
echo "Building the Docker image..."
docker build -t app .
if [ $? -ne 0 ]; then
    echo "Error: Failed to build the Docker image."
    exit 1
fi

# Run the Docker container
echo "Running the Docker container..."
docker run -p 80:5000 app
if [ $? -ne 0 ]; then
    echo "Error: Failed to run the Docker container."
    exit 1
fi

echo "Deployment successful."
exit 0
