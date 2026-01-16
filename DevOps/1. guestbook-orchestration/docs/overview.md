# Project Overview

This project implements a simple Guestbook web application
containerized with Docker and orchestrated using Kubernetes.

The main goal is to demonstrate practical orchestration concepts
commonly used in production environments, including deployment
strategies, autoscaling, and rollback mechanisms.

---

## Application Architecture

The Guestbook application consists of a lightweight web frontend
that allows users to submit text entries, which are rendered
dynamically on the page.

The application is deployed as a Kubernetes Deployment and exposed
through a Service. Resource constraints and autoscaling policies
are applied to simulate real-world workloads.

---

## Containerization Strategy

The application images are built using Docker with multi-stage
builds to reduce final image size and improve security.

Two application versions are provided:

- **v1**: Initial deployment version
- **v2**: Updated version used to demonstrate rolling updates
  and rollback behavior

---

## Kubernetes Orchestration

The Kubernetes configuration includes:

- Deployments with rolling update strategies
- Resource requests and limits
- Horizontal Pod Autoscaler (HPA) based on CPU utilization
- Rollout history inspection and controlled rollback

These configurations allow the application to automatically scale
under load and safely transition between versions.

---

## Purpose

This repository is structured as a portfolio-ready project to
showcase hands-on experience with container orchestration and
Kubernetes operational workflows.
