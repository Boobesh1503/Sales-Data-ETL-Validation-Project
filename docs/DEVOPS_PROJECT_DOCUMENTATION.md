# Sales Data ETL Validation – DevOps Automation Project

## 1. Project Overview

This project focuses on validating sales data through automated testing and implementing a DevOps pipeline to automate testing, Docker image creation, publishing, and cloud-based test execution.

The project combines Python-based ETL validation, automated testing with Pytest, GitHub Actions CI/CD, Docker containerization, GitHub Container Registry (GHCR), AWS EC2, and AWS Systems Manager (SSM).

The primary objective is to detect data quality issues automatically and execute validation tests consistently across local and cloud environments.

---

## 2. Project Objectives

- Validate sales datasets for data quality issues.
- Automate ETL validation using Python.
- Create automated test cases using Pytest.
- Integrate tests into GitHub Actions CI.
- Containerize the validation application using Docker.
- Publish Docker images to GitHub Container Registry.
- Deploy and execute the container on AWS EC2.
- Automate cloud execution using AWS Systems Manager.
- Implement a GitHub Actions deployment workflow.

---

## 3. Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Testing Framework | Pytest |
| Version Control | Git |
| Source Code Hosting | GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | GitHub Container Registry (GHCR) |
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| Remote Execution | AWS Systems Manager (SSM) |
| Operating System | Amazon Linux 2023 |
| Instance Type | t3.micro |
| AWS Region | ap-southeast-2 |

---

## 4. Data Validation

The project validates sales data and identifies common data quality issues.

### Validation checks

- Duplicate Order IDs
- Missing Customer IDs
- Missing Order Dates
- Missing Quantity values
- Missing City values
- Negative Unit Prices
- Invalid Discount Percentages

The dataset contains intentionally introduced data-quality issues to test the validation process.

---

## 5. Python Automated Testing

Python scripts are used to perform data validation.

Pytest is used to automate the execution of validation test cases.

### Test coverage

The automated test suite currently contains:

**14 automated test cases**

The tests validate different data-quality scenarios and ensure that the validation logic behaves as expected.

### Local test execution

```bash
python -m pytest tests/ -v
```

Expected result:

```text
14 passed
```

---

## 6. Continuous Integration – GitHub Actions

A GitHub Actions workflow automatically executes the automated tests whenever changes are pushed to the configured branch.

### CI Pipeline Process

1. Developer pushes code to GitHub.
2. GitHub Actions workflow is triggered.
3. Python environment is configured.
4. Dependencies are installed.
5. Automated ETL validation tests are executed.
6. Workflow reports success or failure.

### Workflow file

```text
.github/workflows/ci.yml
```

The CI pipeline ensures that code changes do not break existing validation functionality.

---

## 7. Docker Containerization

The application is containerized using Docker.

Docker provides a consistent environment for running the validation application locally and on cloud infrastructure.

### Dockerfile

The Dockerfile defines:

- Base Python image
- Working directory
- Dependency installation
- Application files
- Test execution command

### Build Docker Image

```bash
docker build -t sales-etl-validation .
```

### Run Docker Container

```bash
docker run --rm sales-etl-validation
```

The container executes the automated ETL validation test suite.

---

## 8. GitHub Container Registry

The Docker image is published to GitHub Container Registry.

### Image Repository

```text
ghcr.io/boobesh1503/sales-etl-validation
```

### Image Tag

```text
latest
```

### Pull Docker Image

```bash
docker pull ghcr.io/boobesh1503/sales-etl-validation:latest
```

### Run Published Image

```bash
docker run --rm ghcr.io/boobesh1503/sales-etl-validation:latest
```

The image can be pulled and executed on different environments without requiring the entire source code repository.

---

## 9. Docker Build and Publish Automation

A GitHub Actions workflow automatically builds and publishes the Docker image to GHCR.

### Workflow Process

1. Code is pushed to GitHub.
2. GitHub Actions starts the Docker publishing workflow.
3. Docker image is built.
4. Image is tagged.
5. Image is published to GHCR.

### Workflow File

```text
.github/workflows/docker-publish.yml
```

This automation removes the need to manually build and publish Docker images after every code update.

---

## 10. AWS EC2 Infrastructure

An Amazon EC2 instance was created to execute the ETL validation container remotely.

### EC2 Configuration

| Configuration | Value |
|---|---|
| Instance Name | sales-etl-validation-server |
| Instance Type | t3.micro |
| Operating System | Amazon Linux 2023 |
| Region | ap-southeast-2 |
| Container Runtime | Docker |

Docker was installed and configured on the EC2 instance.

---

## 11. Docker Execution on EC2

The EC2 instance was configured to pull the published Docker image from GHCR.

### Pull Image

```bash
docker pull ghcr.io/boobesh1503/sales-etl-validation:latest
```

### Execute Validation

```bash
docker run --rm ghcr.io/boobesh1503/sales-etl-validation:latest
```

The Docker container successfully executed the automated test suite on the EC2 instance.

### Validation Result

```text
14 tests passed
```

---

## 12. AWS Systems Manager (SSM)

AWS Systems Manager was configured to enable remote command execution on the EC2 instance without requiring SSH access for deployment automation.

### Configuration

- Systems Manager Agent
- EC2 IAM Role
- AmazonSSMManagedInstanceCore policy
- Managed instance registration

### EC2 IAM Role

```text
SalesETL-EC2-SSM-Role
```

The role provides the EC2 instance with the necessary permissions to communicate with AWS Systems Manager.

### Verification

The EC2 instance was successfully registered as a managed node.

The SSM Ping Status was verified as:

```text
Online
```

---

## 13. GitHub Actions AWS Authentication

GitHub Actions requires AWS credentials to execute deployment commands.

An IAM user was created for GitHub Actions deployment.

### IAM User

```text
github-deployment-user
```

### Permissions

The IAM user was provided permissions required for:

- Sending Systems Manager commands
- Retrieving command execution results
- Listing command invocations

### GitHub Repository Secrets

The following secrets were configured in GitHub:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
EC2_INSTANCE_ID
```

Sensitive credentials are stored as GitHub Actions secrets and are not hardcoded into the repository.

---

## 14. Automated EC2 Deployment Workflow

The deployment workflow is designed to automatically execute ETL validation on EC2 after the Docker image publishing workflow completes successfully.

### Deployment Process

1. Docker publishing workflow completes.
2. Deployment workflow is triggered.
3. GitHub Actions configures AWS credentials.
4. AWS Systems Manager sends a command to EC2.
5. EC2 pulls the latest Docker image.
6. Docker container executes ETL validation tests.
7. GitHub Actions retrieves the command output.
8. Deployment workflow reports success or failure.

### Workflow File

```text
.github/workflows/deploy-ec2.yml
```

### Remote Commands

```bash
docker pull ghcr.io/boobesh1503/sales-etl-validation:latest

docker run --rm ghcr.io/boobesh1503/sales-etl-validation:latest
```

The workflow is configured for automated remote execution. End-to-end automatic deployment verification is pending.

---

## 15. Project Architecture

```text
Developer
   |
   | Git Push
   v
GitHub Repository
   |
   v
GitHub Actions CI
   |
   | Run Python Tests
   | 14 Tests
   v
CI Success
   |
   v
Docker Build Workflow
   |
   | Build Docker Image
   v
GitHub Container Registry
   |
   | Publish Image
   v
Deployment Workflow
   |
   | AWS Credentials
   v
AWS Systems Manager
   |
   | Send Remote Command
   v
Amazon EC2
   |
   | Docker Pull
   v
Docker Container
   |
   | Execute Validation
   v
ETL Validation Tests
   |
   v
Test Results
```

---

## 16. Repository Structure

```text
Sales-Data-ETL-Validation-Project/
│
├── tests/
│   └── test_etl_validation.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-publish.yml
│       └── deploy-ec2.yml
│
├── Dockerfile
├── .dockerignore
├── requirements-dev.txt
├── find_data_issues.py
├── sales_data.csv
└── README.md
```

---

## 17. Security Considerations

- AWS credentials are stored in GitHub Secrets.
- Credentials are not hardcoded in source code.
- EC2 remote execution uses AWS Systems Manager.
- IAM permissions are configured for deployment-related operations.
- Docker images are published through GitHub Container Registry.
- Sensitive configuration values should never be committed to GitHub.

---

## 18. Troubleshooting

### Docker Image Pull Failure

Verify:

- Docker is running.
- GHCR image name is correct.
- Image is publicly accessible or authentication is configured.

### Docker Container Execution Failure

Check:

```bash
docker logs <container_id>
```

### EC2 SSM Connection Issues

Verify:

- SSM Agent is running.
- EC2 IAM role is attached.
- `AmazonSSMManagedInstanceCore` permissions are available.
- Instance appears under Systems Manager Managed Nodes.
- Ping Status is Online.

### GitHub Actions AWS Authentication Failure

Verify the GitHub repository secrets:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
EC2_INSTANCE_ID
```

### Deployment Workflow Failure

Check the GitHub Actions workflow logs and AWS Systems Manager command execution output.

---

## 19. Current Project Status

| Component | Status |
|---|---|
| ETL Validation Logic | Completed |
| Python Test Suite | Completed |
| 14 Automated Tests | Passing |
| GitHub Actions CI | Completed |
| Docker Build | Completed |
| Local Docker Execution | Completed |
| GHCR Image Publishing | Completed |
| AWS EC2 Setup | Completed |
| Docker on EC2 | Completed |
| EC2 Docker Test Execution | Verified |
| AWS Systems Manager | Online |
| GitHub AWS Secrets | Configured |
| Automated EC2 Deployment Workflow | Configured |
| End-to-End Automated Deployment | Pending Verification |

---

## 20. Conclusion

This project demonstrates an end-to-end DevOps implementation for an ETL data-validation application.

It integrates automated testing, CI pipelines, Docker containerization, image publishing, cloud infrastructure, and remote command execution.

The implementation demonstrates practical experience with Python testing, GitHub Actions, Docker, GHCR, AWS EC2, IAM, and AWS Systems Manager.

The project provides a foundation for expanding into more advanced DevOps practices such as monitoring, logging, infrastructure as code, security scanning, and production deployment automation.
