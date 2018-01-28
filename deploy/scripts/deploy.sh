#!/usr/bin/env bash


KEYS_DIR="$(dirname "$0")/../../keys"
gpg ${KEYS_DIR}/env.sh.gpg
source ${KEYS_DIR}/env.sh

echo "Push docker image to the Docker Hub..."
docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"
docker push metallica127/infinity:latest
