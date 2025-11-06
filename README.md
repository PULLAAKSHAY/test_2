# CI/CD Flask App

This is a simple Flask web application that demonstrates a CI/CD pipeline using GitHub Actions to automate testing and deployment to an AWS EC2 instance.

## CI/CD Pipeline

The CI/CD pipeline is composed of two GitHub Actions workflows: one for Continuous Integration (CI) and one for Continuous Deployment (CD).

### Continuous Integration (CI)

The CI workflow is defined in the `.github/python-app.yml` file and is triggered on every push to a branch other than `main` and on every pull request to `main`. The purpose of this workflow is to ensure that new code is tested before it is merged into the `main` branch.

The CI workflow performs the following steps:

1.  **Checkout Code**: Checks out the repository's code.
2.  **Set up Python**: Sets up the specified version of Python.
3.  **Install Dependencies**: Installs the project's dependencies from the `requirements.txt` file.
4.  **Run Tests**: Runs the test suite using `pytest`.

### Continuous Deployment (CD)

The CD workflow is defined in the `.github/workflows/deploy.yml` file and is triggered on every push to the `main` branch. The purpose of this workflow is to automatically deploy the latest version of the application to the EC2 instance.

The CD workflow performs the following steps:

1.  **Checkout Code**: Checks out the repository's code.
2.  **SSH and Deploy**:
    *   Connects to the EC2 instance via SSH using the provided secrets (`EC2_HOST`, `EC2_USERNAME`, `EC2_SSH_KEY`).
    *   Navigates to the project directory.
    *   Pulls the latest changes from the `main` branch.
    *   Executes the `deploy.sh` script to update the application.

### Deployment Script (`deploy.sh`)

The `deploy.sh` script is responsible for setting up the environment and running the application on the EC2 instance. It performs the following steps:

1.  **Update System**: Updates the system's package list.
2.  **Install Dependencies**: Installs Python, pip, and venv.
3.  **Create Virtual Environment**: Creates a Python virtual environment.
4.  **Install Python Dependencies**: Installs the required Python packages from `requirements.txt`.
5.  **Initialize Database**: Initializes the SQLite database.
6.  **Start Application**: Starts the Flask application using Gunicorn.

### Secrets

To enable the CD workflow, you must configure the following secrets in your GitHub repository's settings:

*   `EC2_HOST`: The public IP address or DNS name of your EC2 instance.
*   `EC2_USERNAME`: The username for connecting to your EC2 instance (e.g., `ubuntu`, `ec2-user`).
*   `EC2_SSH_KEY`: The private SSH key for connecting to your EC2 instance.

## Local Development

To run the application locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```
2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Initialize the database**:
    ```bash
    flask --app app/app.py initdb
    ```
5.  **Run the application**:
    ```bash
    flask --app app/app.py run
    ```

The application will be available at `http://127.0.0.1:5000`.
