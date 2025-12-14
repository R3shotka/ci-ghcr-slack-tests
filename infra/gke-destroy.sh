#!/usr/bin/env bash
set -euo pipefail
kind delete cluster --name cd-kind || true
