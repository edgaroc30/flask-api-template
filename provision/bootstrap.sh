#!/usr/bin/env bash

USER=/home/vagrant

# Get updates and upgrade
# sudo apt-get update
# sudo apt upgrade -y

# Development files
sudo rm -rf /srv/app
sudo mkdir /srv/app
sudo ln -s /vagrant/app /srv/app

# Setting up api-rebuild bash profile
sudo rm $USER/.bash_profile
sudo cp $USER/vagrant $USER/.bash_profile
sudo rm $USER/vagrant

# Print the VM IP address
ip addr show eth1 | egrep "inet\ " | cut -f1 -d "/" | cut -f2 -d "t"