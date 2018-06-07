#!/bin/bash

rm /tmp/jnotebook.log; 

/home/rendong/anaconda3/envs/dl4cv/bin/jupyter notebook --ip='*' --port=80 --no-browser --allow-root >& /tmp/jnotebook.log &
# jupyter notebook --ip='*' --no-browser  >& /tmp/jnotebook.log & 
