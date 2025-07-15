# 🚀 DevOps Pipeline: Docker + GitHub Actions + Kubernetes

A minimal CI/CD demo that builds a Docker image on push, pushes to Docker Hub, and deploys locally via Minikube.

---

## 🛠️ Tech Stack

- **GitHub Actions** (CI)
- **Docker** (container)
- **Kubernetes** + **Minikube** (orchestration)

---

## ⚡ Quick Start

1. **Clone & configure**  
   ```bash
   git clone https://github.com/yourusername/devops-pipeline.git
   cd devops-pipeline

2. **Build & Push image**
docker build -t yourusername/yourapp .
docker push yourusername/yourapp

3. **Deploy locally**
minikube start
kubectl apply -f deployment.yaml service.yaml
minikube service myapp-service

## 📂 Project Structure
.
├── app/                # Your code
├── Dockerfile
├── .github/workflows/  # CI config
├── deployment.yaml
└── service.yaml

## 🔒 Secrets
DOCKER_USERNAME
DOCKER_PASSWORD
