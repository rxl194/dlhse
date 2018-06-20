#!/bin/bash

# virtual frame buffer
# https://github.com/processing/processing/wiki/Running-without-a-Display


sudo apt-get install xvfb libxrender1 libxtst6 libxi6 

java -version
#sudo apt-get install default-jdk
# or
#sudo apt-get install default-jre

sudo Xvfb :1 -screen 0 1024x768x24 </dev/null &
export DISPLAY=":1"


## install GLU library
sudo apt-get install freeglut3-dev
pip install pyopengl

