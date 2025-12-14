#!/usr/bin/env bash
set -euo pipefail
kind create cluster --name cd-kind
kubectl create namespace app || true
