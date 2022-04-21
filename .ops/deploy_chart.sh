#!/usr/bin/env sh

DIRECTORY=$1
HELM_TIMEOUT=$2
KUBECONFIG=$3
KUBECONTEXT=$4
KUBE_NAMESPACE=$5
ENVIRONMENT=$6
HELM_IMAGE_TAG_VALUE=$7
RELEASE_NAME=$8

COMMIT_HASH=`git log --pretty=format:"%H" -n 1 -- $DIRECTORY`
IMAGE_TAG=${CI_COMMIT_SHA:0:8}
CHART_PATH="$DIRECTORY/.helm"
GLOBAL_SECRETS="$CHART_PATH/secrets.yaml"
ENVIRONMENT_DIR="$CHART_PATH/environments/${ENVIRONMENT}"
HELM_VALUES_FILE="$ENVIRONMENT_DIR/values.yaml"
HELM_SECRETS_FILE="$ENVIRONMENT_DIR/secrets.yaml"

helm secrets upgrade \
    --kubeconfig="$KUBECONFIG" \
    --kube-context="$KUBECONTEXT" \
    --install \
    --wait \
    --history-max 4 \
    --timeout="$HELM_TIMEOUT" \
    --namespace="$KUBE_NAMESPACE" \
    --create-namespace \
    --values="$GLOBAL_SECRETS" \
    --values="$HELM_VALUES_FILE" \
    --values="$HELM_SECRETS_FILE" \
    --set $HELM_IMAGE_TAG_VALUE=$IMAGE_TAG \
    $RELEASE_NAME \
    $CHART_PATH
