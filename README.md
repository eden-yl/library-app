# 📚 The Grand Tour of Libraries Web Service (Dockerized)

A minimalist web service built with Flask that showcases beautiful libraries worldwide, now containerized using Docker for simplified deployment and environment consistency.

## 🔗 Quick Access (Live Deployment)

The service is deployed on Render using the official Docker image:

**[https://library-app-9est.onrender.com](https://library-app-9est.onrender.com)**

-----

## ✨ Features

  * **Containerized:** Packaged with Docker for dependency isolation and seamless portability.
  * **Notion-Like Design:** Clean, distraction-free interface using modern CSS.
  * **Python/Flask Backend:** Lightweight application logic running on **Gunicorn**.
  * **Dynamic Routing:** Each library card links to a specific detail page.

-----

## 🛠️ Local Development Setup (Via Docker)

The easiest way to run this project is by using **Docker**. This eliminates the need to manually install Python dependencies.

### 1\. Prerequisites

You need **Docker Desktop** installed on your system (available for Windows, macOS, and Linux).

### 2\. Clone the Repository and Build the Image

Open your terminal (PowerShell, Command Prompt, or Git Bash) in the project directory.

```bash
# Clone the repository (if you haven't already)
git clone [YOUR_REPO_URL_HERE]
cd library-service

# Build the Docker image using the instructions in the Dockerfile
docker build -t local/library-service:latest .
```

### 3\. Run the Container

Run the newly built image, mapping the container's internal port (`8000`) to a convenient local port (`5000`):

```bash
docker run -p 5000:8000 local/library-service:latest
```

The service will be available at: **[http://localhost:5000/](https://www.google.com/search?q=http://localhost:5000/)**

-----

## 🐳 Deployment & Containerization

This service is ready for modern container orchestration platforms (like Render or Kubernetes).

### Docker Image Details

| Detail | Value |
| :--- | :--- |
| **Base Image** | `python:3.11-slim` |
| **Container Port** | `8000` (Exposed via `EXPOSE 8000`) |
| **Start Command** | `gunicorn --bind 0.0.0.0:8000 app:app` |
| **Registry Path** | `[YOUR_DOCKERHUB_USERNAME]/library-service:v1` |

### Publishing Updates

To deploy a new version to the public site:

1.  Build the new image with an incremented tag (e.g., `v2`):
    ```bash
    docker build -t [YOUR_DOCKERHUB_USERNAME]/library-service:v2 .
    ```
2.  Push the new image to Docker Hub:
    ```bash
    docker push [YOUR_DOCKERHUB_USERNAME]/library-service:v2
    ```
3.  Go to the **Render Dashboard** and update the service's **Image URL** to the new tag (`:v2`).

-----

## ☸️ Kubernetes Configuration

Configuration files for deploying this container onto a Kubernetes cluster (tested with Minikube) are located in the `k8s/` directory:

  * **`deployment.yaml`**: Defines the desired state of the application Pods (replicas, image name, resource limits).
  * **`service.yaml`**: Exposes the Pods via a stable network endpoint (`LoadBalancer` type).

-----