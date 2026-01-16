# Technical Capability Mapping

This document maps the implemented components of the project
to concrete technical capabilities demonstrated through code,
configuration, and execution evidence.

---

## Container Image Build and Registry Management

**Capability demonstrated:**
- Building container images using Docker
- Versioning application images
- Pushing images to a container registry

**Implementation:**
- `docker/Dockerfile.v1`
- `docker/Dockerfile.v2`

**Evidence:**
- `evidence/container-registry/Dockerfile.png`
- `evidence/container-registry/crimages.png`

---

## Kubernetes Application Deployment

**Capability demonstrated:**
- Creating Kubernetes Deployments and Services
- Managing application lifecycle within a cluster
- Applying resource requests and limits

**Implementation:**
- `k8s/deployment-guestbook-v1.yaml`
- `k8s/service-guestbook.yaml`

**Evidence:**
- `evidence/frontend-v1/app.png`

---

## Horizontal Pod Autoscaling (Operational)

**Capability demonstrated:**
- Configuring autoscaling using CPU-based metrics
- Observing replica scaling under load
- Operating Kubernetes workloads dynamically

**Implementation:**
- Autoscaling configured via `kubectl autoscale`

**Evidence:**
- `evidence/autoscaling/hpa.png`
- `evidence/autoscaling/hpa2.png`

---

## Rolling Updates

**Capability demonstrated:**
- Updating application versions without downtime
- Managing versioned deployments
- Inspecting rollout history

**Implementation:**
- `k8s/deployment-guestbook-v2.yaml`

**Evidence:**
- `evidence/rolling-update/upguestbook.png`
- `evidence/rolling-update/deployment.png`
- `evidence/rolling-update/up-app.png`

---

## Deployment Rollback

**Capability demonstrated:**
- Inspecting deployment revision history
- Rolling back to a previous stable version
- Verifying ReplicaSet changes after rollback

**Implementation:**
- Kubernetes rollout undo operations

**Evidence:**
- `evidence/rollback/rev.png`
- `evidence/rollback/rs.png`

---

## Distributed Application Architecture

**Capability demonstrated:**
- Deploying multi-component applications
- Managing backend datastore services
- Understanding service discovery and pod communication

**Implementation:**
- `k8s/deployment-redis-master.yaml`
- `k8s/service-redis-master.yaml`
- `k8s/deployment-redis-slave.yaml`
- `k8s/service-redis-slave.yaml`
