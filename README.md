# CI/CD DevOps Pipeline: Docker + GitHub Actions + Kubernetes
A complete CI/CD pipeline that builds, tests, pushes a Dockerized app using **GitHub Actions**, and deploys it to a local **Kubernetes** cluster with **Minikube**.

---

## Tech Stack
- **GitHub Actions** (CI)
- **Docker** (container)
- **Kubernetes** + **Minikube** (orchestration)

## Features

- ✅ Automated Docker build & push on every commit  
- ✅ Kubernetes deployment using YAML config  
- ✅ Local app access via `minikube service`  
- ✅ Uses GitHub Secrets for Docker auth

## ⚙️ How to Run (Local Dev)

```bash
# 1. Start Kubernetes cluster
minikube start

# 2. Deploy app
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 3. Access in browser
minikube service myapp-service

## Secrets required
DOCKER_USERNAME
DOCKER_PASSWORD
