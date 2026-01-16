# Guestbook Application – Kubernetes Orchestration

This repository contains a containerized Guestbook web application
designed to demonstrate Kubernetes orchestration concepts in a
production-style environment.

The project showcases container image builds, Kubernetes deployments,
autoscaling behavior, rolling updates, and rollback operations.

---

## Project Overview

The Guestbook application is a simple web frontend that allows users
to submit text entries which are dynamically rendered on the page.

The application is deployed on Kubernetes using Deployments and
Services, with Redis used as a backend datastore to demonstrate a
multi-component distributed architecture.

---

## Repository Structure

- src/ Application source code (v1 and v2)
- docker/ Dockerfiles for container images
- k8s/ Kubernetes manifests (deployments and services)
- docs/ Technical documentation
- evidence/ Execution and validation screenshots


---

## Key Concepts Demonstrated

- Docker multi-stage builds
- Kubernetes Deployments and Services
- Horizontal Pod Autoscaling (operational)
- Rolling updates and rollback
- Multi-component application architecture

---

## Documentation

- Project overview: `docs/overview.md`
- Technical capability mapping: `docs/evaluation-mapping.md`
- Execution evidence: `evidence/`

---

## Notes

This repository is intended as a portfolio project to demonstrate
hands-on experience with containerization and Kubernetes orchestration.
