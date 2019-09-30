# Flask API template

A simple template using Vagrant and Docker for a Flask API

Make sure to change the name and Paths in the bash_profile if there are changes in the name of the app or the available ports.The whole API should remain in the app folder

### Rebuild the docker api container

The Flask API can be rebuild by using
```
vagrant ssh -c api-rebuild
```
### Rebuild the api documentation using aglio

The aglio documentation works using node and the set up of the whole vagrant machine might take a while since it requires node. To regenerate the documentation:
```
vagrant ssh -c apidocs-rebuild
```

### Get the IP address of the machine

To easily get the IP address that the machine was assigned the following command will work
```
vagrant ssh -c get-ip
```

### Using Conda

If you are using Conda locally it will help to define the library dependencies and find any possible issues with the libraries
```
conda create -n flask-api python=3.6 pip
conda activate flask-api
pip install -r app/requirements.txt
```

## External references

[Vagrant docs](https://www.vagrantup.com/docs/cli/)
[Docker docs](https://docs.docker.com/engine/reference/commandline/cli/)
[Aglio docs](https://www.npmjs.com/package/aglio)
[Flask docs](https://flask.palletsprojects.com/en/1.1.x/)