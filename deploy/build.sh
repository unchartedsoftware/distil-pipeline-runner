#!/bin/bash

source ./config.sh

# builds distil docker image
docker build \
    --squash \
    --build-arg SSH_PRIVATE_KEY="$(cat $TIMESERIES_LOADER_KEY_LOC)" \
    --tag docker.uncharted.software/$DOCKER_IMAGE_NAME:${DOCKER_IMAGE_VERSION} \
    --tag docker.uncharted.software/$DOCKER_IMAGE_NAME:latest ..
