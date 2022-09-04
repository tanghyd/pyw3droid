# W3Droid - Python RL Environment
[![Discord](https://img.shields.io/discord/591914197219016707.svg?color=7289da&label=Project%20Discord&logo=discord&style=flat-square)](https://discord.gg/qfXneBxBed)

Community Experiment on A WarCraft 3 AI

---
## Project Scope

### API 

- @Pad
- @Helpstone
- @War3NEFans

#### Ideas

- Simulate a game in faster than real time

### Model

- @C5ipo7i
- @freshwind
- @tanghyd

### Maps

- @theOCdrummer


---
## Setup 

**NOTE:** The following has only been tested on Ubuntu, please let us know if these commands do 
not work on your operating system.


First, clone the repository from GitHub, i.e.:

    git clone https://github.com/FreeTymeKiyan/W3Droid.git
    cd W3Droid


After cloning, installation of this Python package in a local virtual environment 
should be as simple as executing one of the following sets of commands:

### Virtualenv

If you are using virtualenv with a prepared Python 3 installation, we can run the 
following to create a virtual environment with the name `<venv>`.

    python -m venv <venv>       # or python3, python3.10, etc.
    source <venv>/bin/activate  # activate virtual environment
    pip install --upgrade pip   # optional: pip may already be its latest version
    pip install .               # optional: use the -e flag for --editable mode


### Conda

If you are using conda as an environment manager, then we can create a conda
virtual environment with latest stable version of Python3 called `<venv>` as follows:

    conda create -n <venv> python=3 pip conda-build
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

### Jupyter Notebook Kernel

If the user would like to use this virtual environment in a Jupyter notebook kernel, we can execute the following:

  ```
  # add virtual environment to jupyter notebook kernels (can change --name)
  pip install ipykernel                             # or conda install ipykernel
  python -m ipykernel install --user --name=spiir
  ```
