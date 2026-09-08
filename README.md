# Dockerized Flask App — Full Production Deployment Pipeline

A complete, real-world deployment setup: containerized app, reverse proxy, free SSL, and automated CI/CD — deployed on AWS EC2, provisioned entirely as code with Terraform.

**Live demo:** https://giriwithdevops.duckdns.org

## What this demonstrates

- **Containerization** — Flask app + PostgreSQL, orchestrated with Docker Compose, with a persistent volume so database data survives container restarts
- **Reverse proxy** — Nginx sits in front of the app, terminating SSL and forwarding traffic internally; the app and database are never directly exposed to the internet
- **Free, trusted HTTPS** — SSL certificate issued and auto-renewable via Let's Encrypt / Certbot
- **CI/CD** — GitHub Actions automatically deploys on every push to `main` (SSH-based deploy to the EC2 instance — no manual server access needed)
- **Infrastructure as Code** — the entire AWS environment (EC2 instance, security group, Elastic IP) is defined in Terraform and reproducible with a single `terraform apply`

## Architecture

```
                    ┌─────────────┐
   Internet ──────▶ │    Nginx    │  (ports 80/443, SSL termination)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Flask app  │  (internal only)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  PostgreSQL │  (internal only, persistent volume)
                    └─────────────┘
```

## Stack

| Layer | Tool |
|---|---|
| App | Flask + PostgreSQL |
| Containerization | Docker, Docker Compose |
| Reverse proxy / SSL | Nginx, Let's Encrypt (Certbot) |
| CI/CD | GitHub Actions (SSH deploy) |
| Cloud | AWS EC2 |
| Infrastructure as Code | Terraform |
| DNS | DuckDNS |

## Repo structure

```
.
├── app.py                   # Flask application
├── Dockerfile
├── docker-compose.yml       # app + db + nginx + certbot services
├── nginx.conf                # reverse proxy + SSL config
├── .github/workflows/
│   └── deploy.yml           # CI/CD: auto-deploy on push to main
└── terraform/
    └── main.tf               # EC2 + security group + Elastic IP, as code
```

## Running it yourself

```bash
git clone https://github.com/<your-username>/docker-practice.git
cd docker-practice
docker compose up -d --build
curl http://localhost:8080
```

## About

Built as a hands-on demonstration of end-to-end DevOps deployment practices — from a working local Docker Compose setup all the way to a production-style, HTTPS-secured, auto-deploying cloud environment.

**Available for freelance work:** containerizing applications, setting up CI/CD pipelines, reverse proxy + SSL configuration, and cloud deployment (AWS). Get in touch via [Upwork/Fiverr link] or [email].
