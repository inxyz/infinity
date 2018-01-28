#!/usr/bin/env bash


KEYS_DIR="$(dirname "$0")/../../keys"

echo ${keys_password} | gpg --passphrase-fd 0 ${KEYS_DIR}/env.sh.gpg
#gpg ${KEYS_DIR}/env.sh.gpg
source ${KEYS_DIR}/env.sh

echo "Push docker image to the Docker Hub..."
docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"
docker push metallica127/infinity:dev
