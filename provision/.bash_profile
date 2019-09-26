#!/bin/bash

function api-rebuild () {
	CONTAINER_API="flask-api"
	APP_PATH="/srv/app/app"
	cd $APP_PATH  #PATH
	docker kill $(docker ps -q --filter ancestor=$CONTAINER_API)
	docker rm  $(docker ps -q --filter ancestor=$CONTAINER_API)
	docker build -t $CONTAINER_API:latest .
	docker run -d -p 80:5000 $CONTAINER_API
 	}

function api-doc-rebiuld () {
	DOCUMENTATION_PATH="/srv/aglio/aglio"
	cd $DOCUMENTATION_PATH
	aglio -i input.apib -o output.html
	}