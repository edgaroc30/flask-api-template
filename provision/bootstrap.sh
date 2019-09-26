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
# sudo rm $HOME/.bash_profile
# sudo cp $HOME/vagrant $HOME/.bash_profile
# sudo rm $HOME/vagrant

# Print the VM IP address
ip addr show eth1 | egrep "inet\ " | cut -f1 -d "/" | cut -f2 -d "t"