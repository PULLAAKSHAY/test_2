#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update the package repository and install Python and pip
echo "Updating system and installing Python..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install the required Python packages
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Initialize the database
echo "Initializing the database..."
flask --app app/app.py initdb

# Start the application with Gunicorn
echo "Starting the application with Gunicorn..."
gunicorn --bind 0.0.0.0:8000 app.app:app &

echo "Deployment complete. The application is running on port 8000."
