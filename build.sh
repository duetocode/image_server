#!/bin/sh

VERSION=$(cat version)
docker build -t data-image-server:$VERSION -t registry.service.motoilet.cn/data-image-server:$VERSION .
