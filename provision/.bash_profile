#!/bin/bash test
CONTAINER="flask-api"
APP_PATH="/srv/app/app"

function api-rebuild() {
	 cd $APP_PATH  #PATH
	 docker kill $(docker ps -q --filter ancestor=$CONTAINER)
	 docker rm  $(docker ps -q --filter ancestor=$CONTAINER)
	 docker build -t $CONTAINER:latest .
	 docker run -d -p 80:5000 $CONTAINER
 	 }