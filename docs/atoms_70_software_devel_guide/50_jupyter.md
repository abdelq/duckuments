# Jupyter  {#jupyter status=draf}

## Installation {#jupyter-install}

Pull the branch 1710-place-recognition

    $ cd duckietown
    $ git pull

Source environment:

    $ source environment.sh

Remove previous installations:

    $ sudo apt remove ipython ipython-notebook

Then run:

    $ pip install --user jupyter IPython==5.0

Check the versions are correct:

    $ which ipython

    /home/andrea/.local/bin/ipython

Check the version is correct:

    $ ipython --version

    5.0.0

## Configuration

Set a password:

    $ jupyter notebook password


## Running it

    $ jupyter notebook --notebook-dir=$DUCKIETOWN_ROOT/catkin_ws/src/75-notebooks



## Extra configuration for virtual machines


Create a configuration file:

    $ jupyter notebook --generate-config

Edit the file `~/.jupyter/jupyter_notebook_config.py`.

Uncomment and change the line:

    #c.NotebookApp.ip = 'localhost'

Into:

    c.NotebookApp.ip = '*'
