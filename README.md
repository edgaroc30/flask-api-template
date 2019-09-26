# Flask API template

A simple template using Vagrant and Docker for a Flask API

The Flask API can be rebuild by using
```
vagrant ssh -c api-rebuild
```
Make sure to change the name and Paths in the bash_profile if there are changes in the name of the app or the available ports

The whole application should remain in the app folder

If you are using Conda locally it will help to define the library dependencies and find any possible issues with the libraries
```
conda create -n flask-api python=3.6 pip
conda activate flask-api
pip install -r app/requirements.txt
```

The aglio documentation works using node and the set up of the whole vagrant machine might take a while since it requires node. To regenerate the documentation:
```
vagrant ssh -c doc-rebuild
```