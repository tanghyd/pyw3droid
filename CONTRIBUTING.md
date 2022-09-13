# W3Droid - Python RL Environment
[![Discord](https://img.shields.io/discord/591914197219016707.svg?color=7289da&label=Project%20Discord&logo=discord&style=flat-square)](https://discord.gg/qfXneBxBed)

Welcome to the developer contribution guide for `pyw3droid`!

## Python Style Guide

We recommend writing Python code in style of [Black](https://github.com/psf/black).

Additionally, a Black formatting check has been added to the `.pre-commit-config.yaml` file.

## Pre-Commit

We use pre-commit to ensure that `git commit` commands are only executed if they 
satisfy the requirements specified in the `.pre-commit-config.yaml` file, to ensure 
code readability and standards. To setup precommit in a new git repository, activate a 
virtual environment of your choice and run:

    # pip install pre-commit    # if precommit is not alraedy installed
    pre-commit install