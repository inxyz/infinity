#!/usr/bin/env bash



gpg ../../keys/env.sh.gpg
source ../../keys/env.sh

echo "Push docker image to the Docker Hub..."
docker login -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"
docker push metallica127/infinity:latest
