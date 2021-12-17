#!/bin/bash -e

#variaveis necessarias para tag e envio
REGISTRY_URL=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
SOURCE_IMAGE="${ECR_REPO}"
TARGET_IMAGE="${REGISTRY_URL}/${ECR_REPO}"
TARGET_IMAGE_LATEST="${TARGET_IMAGE}:latest"
VERSION=`cat appversion`
TARGET_IMAGE_VERSIONED="${TARGET_IMAGE}:${VERSION}"

aws configure set default.region ${AWS_REGION}

#login ecr
#$(aws ecr get-login --no-include-email)

aws ecr get-login-password | docker login --username AWS --password-stdin ${TARGET_IMAGE}

#Envio para o ECR
#---------------#

#enviando a latest
docker tag ${SOURCE_IMAGE} ${TARGET_IMAGE_LATEST}
docker push ${TARGET_IMAGE_LATEST}

#enviando a versionada
docker tag ${SOURCE_IMAGE} ${TARGET_IMAGE_VERSIONED}
docker push ${TARGET_IMAGE_VERSIONED}
