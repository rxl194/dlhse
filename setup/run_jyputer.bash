#!/bin/bash

# rm /tmp/jnotebook.log; 

sudo Xvfb :1 -screen 0 1024x768x24 </dev/null &
export DISPLAY=":1"


/home/rendong/anaconda3/envs/dl4cv/bin/jupyter notebook --ip='*' --port=80 --no-browser --allow-root >& /tmp/jnotebook.log &
# jupyter notebook --ip='*' --no-browser  >& /tmp/jnotebook.log & 
