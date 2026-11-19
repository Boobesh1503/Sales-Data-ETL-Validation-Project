# Sales Data ETL Validation Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![AWS](https://img.shields.io/badge/Cloud-AWS-orange)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-black)

An automated ETL data validation project enhanced with DevOps practices using Python, Pytest, GitHub Actions, Docker, GHCR, AWS EC2, and AWS Systems Manager.

## Project Overview

This project validates sales datasets and identifies data-quality issues using Python-based validation scripts and automated test cases.

The project also implements a DevOps pipeline to automate testing, Docker image building, publishing, and remote execution of validation tests on AWS EC2.

## Key Features

- Sales data validation
- Duplicate record detection
- Null-value validation
- Invalid data detection
- Automated testing using Pytest
- CI pipeline using GitHub Actions
- Docker containerization
- Automated Docker image publishing to GHCR
- AWS EC2 deployment environment
- Remote execution using AWS Systems Manager

## Technology Stack

- Python
- Pytest
- SQL
- Git & GitHub
- GitHub Actions
- Docker
- GitHub Container Registry
- AWS EC2
- AWS Systems Manager
- Amazon Linux 2023

## Data Quality Checks

The project validates:

- Duplicate Order IDs
- Missing Customer IDs
- Missing Order Dates
- Missing Quantity
- Missing City
- Negative Unit Prices
- Invalid Discount Percentages

## Automated Testing

The project contains **14 automated test cases**.

Run tests locally:

```bash
python -m pytest tests/ -v
```

## Docker

Build:

```bash
docker build -t sales-etl-validation .
```

Run:

```bash
docker run --rm sales-etl-validation
```

## GitHub Container Registry

Docker image:

```text
ghcr.io/boobesh1503/sales-etl-validation:latest
```

Pull image:

```bash
docker pull ghcr.io/boobesh1503/sales-etl-validation:latest
```

Run published image:

```bash
docker run --rm ghcr.io/boobesh1503/sales-etl-validation:latest
```

## CI/CD Pipeline

### Continuous Integration

GitHub Actions automatically runs Python validation tests when code changes are pushed.

### Docker Publishing

GitHub Actions builds and publishes the Docker image to GitHub Container Registry.

### Cloud Execution

The Docker image is executed on AWS EC2 using AWS Systems Manager remote commands.

## Architecture

```text
Developer
   |
 Git Push
   |
 GitHub Repository
   |
 GitHub Actions CI
   |
 Automated Tests
   |
 Docker Build
   |
 GHCR
   |
 AWS Deployment Workflow
   |
 AWS Systems Manager
   |
 EC2 Instance
   |
 Docker Container
   |
 ETL Validation
   |
 Test Results
```

## AWS Infrastructure

- EC2: Amazon Linux 2023
- Instance Type: t3.micro
- Region: ap-southeast-2
- Docker installed on EC2
- AWS Systems Manager configured
- EC2 registered as a managed node

## Documentation

Detailed project documentation:

[`docs/DEVOPS_PROJECT_DOCUMENTATION.md`](docs/DEVOPS_PROJECT_DOCUMENTATION.md)

## Project Status

| Component | Status |
|---|---|
| ETL Validation | Completed |
| Python Tests | 14 Passing |
| GitHub Actions CI | Completed |
| Docker | Completed |
| GHCR Publishing | Completed |
| AWS EC2 Setup | Completed |
| SSM Configuration | Online |
| Automated EC2 Workflow | Configured |
| End-to-End Deployment | Verification Pending |

## Author

**Boobesh Prasath**

GitHub: [Boobesh1503](https://github.com/Boobesh1503)
