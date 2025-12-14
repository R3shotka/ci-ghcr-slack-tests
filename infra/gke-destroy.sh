#!/usr/bin/env bash
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
REGION="${REGION:-europe-west1}"
CLUSTER_NAME="${CLUSTER_NAME:-cd-cluster}"

gcloud config set project "$PROJECT_ID"
gcloud container clusters delete "$CLUSTER_NAME" --region "$REGION" --quiet
echo "🗑️ Cluster deleted: $CLUSTER_NAME"
