#!/usr/bin/env bash

USER=/home/vagrant

# Get updates and upgrade
# sudo apt-get update
# sudo apt upgrade -y

# Install Node JS & npm
sudo apt install nodejs -y
sudo apt install npm -y

# Install aglio
sudo npm install -g aglio

# Development files
sudo mkdir /srv/app
sudo ln -s /vagrant/app /srv/app

# Aglio API Blueprint files
sudo mkdir /srv/aglio
sudo ln -s /vagrant/aglio /srv/aglio

# Setting up api-rebuild & doc-rebuild bash profile
sudo rm $HOME/.bash_profile
sudo cp $HOME/vagrant $HOME/.bash_profile
sudo rm $HOME/vagrant
sed -i 's/\r//' $HOME/.bash_profile
source $HOME/.bash_profile

# Rebuild api docs
apidocs-rebuild

# Print IP Address of the machine
get-ip