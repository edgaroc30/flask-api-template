#!/bin/bash

function api-rebuild () {
	CONTAINER_API="flask-api"
	APP_PATH="/srv/app/app"
	cd $APP_PATH
	echo "Removing the Docker container"
	docker kill $(docker ps -q --filter ancestor=$CONTAINER_API)
	docker rm  $(docker ps -q --filter ancestor=$CONTAINER_API)
	echo "Building the Docker container"
	docker build -t $CONTAINER_API:latest .
	echo "Running the Docker container"
	docker run -d -p 80:5000 $CONTAINER_API
	echo "API Rebuild FINISHED"
 	}

function apidocs-rebuild () {
	DOCUMENTATION_PATH="/srv/aglio/aglio"
	cd $DOCUMENTATION_PATH
	aglio -i input.apib -o output.html
	echo "DOCS Rebuild FINISHED"
	}

function get-ip () {
	ip addr show eth1 | egrep "inet\ " | cut -f1 -d "/" | cut -f2 -d "t"
	}