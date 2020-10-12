# SNAB

`SimpleNote as Blog` is an application for publishing your SimpleNote notes as blog posts.

Tag your notes simply with one of the values defined at SN_PUBLISH_TAGS and they will be published.

### Run as a Docker container

The easiest way to test it, is by running the [SNAB Docker image](https://hub.docker.com/repository/docker/arturn/snab).
- Get the [settings.cfg](https://github.com/anebot/snab/blob/master/settings.example.cfg) file and edit with your blog's settings, save it as `settings.cfg`
- Run the container by typing : 
```
docker run -dit --name snab-container -v $(pwd)/settings.cfg:/opt/snab/settings.cfg -p 8080:8080 arturn/snab
```
- Open http://localhost:8080 in your browser.


### Run in local
Otherwise, you can run it in the built-in develop server.

#### Prerequisites

First create a virtualenv with python3

```
virtualenv env --python=python3
```

Before launching the project you have to always activate the environment

```
source env/bin/activate
```

Finally, just install the dependencies

```
pip install -U https://github.com/pallets/flask/archive/master.tar.gz
pip install -r requirements.txt
```

#### Configuring

Configure SNAB by editing the file ```settings.cfg``` file and export ```SNAB_SETTINGS``` enviroment variable pointing to it.
You can see an example of config file at ```settings.example.cfg```

And set FLASK_APP enviroment variable.
```
export FLASK_APP=snab.factory:create_app()
```

#### Running

now you can run snab:
```flask run```

the application will greet you on
http://localhost:5000/

