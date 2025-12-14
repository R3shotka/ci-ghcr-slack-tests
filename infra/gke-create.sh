#!/usr/bin/env bash
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
REGION="${REGION:-europe-west1}"
CLUSTER_NAME="${CLUSTER_NAME:-cd-cluster}"

gcloud config set project "$PROJECT_ID"

# Kubernetes Engine API
gcloud services enable container.googleapis.com

# Autopilot cluster (мінімум ручного керування нодами)
gcloud container clusters create-auto "$CLUSTER_NAME" --region "$REGION"

# kubeconfig для kubectl
gcloud container clusters get-credentials "$CLUSTER_NAME" --region "$REGION"

kubectl create namespace app || true
echo "✅ Cluster created: $CLUSTER_NAME in $REGION"
