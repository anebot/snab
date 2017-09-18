# SNAB

`SimpleNote as Blog` is an application for publishing your SimpleNote notes as blog posts.

Tag your notes simply with one of the values defined at SN_PUBLISH_TAGS and they will be published.

### Prerequisites

First create a virtualenv with python2.7

```
virtualenv env --python=python2.7
```

Before launching the project you have to always activate the environment

```
source env/bin/activate
```

Finally, just install the dependencies

```
pip install -r requirements.txt
```

### Configuring


Configure SNAB by editing the file ```settings.cfg``` file and export ```SNAB_SETTINGS``` enviroment variable pointing to it.
You can see an example of config file at ```settings.example.cfg```

And set FLASK_APP enviroment variable.
```
export FLASK_APP=snab.factory:create_app()
```

## Running

now you can run snab:
```flask run```

the application will greet you on
http://localhost:5000/

