#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update the package repository and install Python, pip, and venv
echo "Updating system and installing Python..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment and install dependencies
echo "Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Initialize the database
echo "Initializing the database..."
flask --app app/app.py initdb

# Start the application with Gunicorn
echo "Starting the application with Gunicorn..."
gunicorn --bind 0.0.0.0:8000 app.app:app &

echo "Deployment complete. The application is running on port 8000."
