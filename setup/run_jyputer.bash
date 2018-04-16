#!/bin/bash

rm /tmp/jnotebook.log; 
/home/rendong/anaconda3/envs/intro-dl/bin/jupyter notebook --ip='*' --port=80 --no-browser --allow-root >& /tmp/jnotebook.log & 
