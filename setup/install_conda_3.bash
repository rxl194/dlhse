#!/bin/bash
# https://github.com/hse-aml/intro-to-dl/blob/master/README.md

# https://github.com/ZEMUSHKA/coursera-aml-docker/blob/master/conda_requirements.txt

#$ conda create --name intro-dl python=3.5
#$ activate intro-dl

conda config --append channels conda-forge
conda config --append channels menpo
conda install --yes --file conda_requirements.txt
