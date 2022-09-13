# pyw3droid - A Warcraft III Python RL Environment

This repository is a Python library used to develop a standardised reinforcement 
learning environment as part of a community-led effort to develop a WarCraft 3 AI. As 
part of the [W3Droid](https://github.com/W3Droid/w3droid) community project, we utilise 
the [W3Droid API](https://github.com/W3Droid/w3droid) which exposes 
functionality for full external control of Warcraft III.

## Contributing

To see more information about contributing to the development of this project, see `CONTRIBUTING.md`.

## Quick Start 

**NOTE:** The following has only been tested on Ubuntu, please let us know if there 
are any issues


First, clone the repository from GitHub, i.e.:

    git clone https://github.com/tanghyd/pyw3droid.git
    cd pyw3droid


After cloning, installation of this Python package in a local virtual environment 
should be as simple as executing one of the following sets of commands:

### Virtualenv

If you are using virtualenv with a prepared Python 3 installation, we can run the 
following to create a virtual environment with the name `<venv>`.

    python -m venv <venv>       # or python3, python3.10, etc.
    source <venv>/bin/activate  # activate virtual environment
    pip install --upgrade pip   # optional: pip may already be its latest version
    pip install .               # optional: use the -e flag for --editable mode

### Jupyter Notebook Kernel

If the user would like to use this virtual environment in a Jupyter notebook kernel 
with the name `w3droid`, we can execute the following:

  ```
  # add virtual environment to jupyter notebook kernels (can change `--name=w3droid`)
  pip install ipykernel                             # or conda install ipykernel
  python -m ipykernel install --user --name=pyw3droid
  ```

### Conda

If you are using conda as an environment manager, then we can create a conda
virtual environment with latest stable version of Python3 called `<venv>` as follows:

    conda create -n <venv> python=3 pip
    conda activate <venv>
    pip install -e .


In general, the above should be sufficient.

If the user wants to install any dependencies via conda, we recommend doing this before 
running the `pip install -e .` command. Installing packages with pip inside an 
activated conda virtual environment may come with some rare edge case problems, and 
packages installed via conda after pip installs may not always play nicely. 
For example, commands like `conda update` will ignore pip installed packages, as it 
only checks conda channels for available updates, so they still need to be updated 
using pip. See: https://stackoverflow.com/q/44265533 for a relevant discussion.

In the future, contributors can develop a better conda distribution solution for this package.
