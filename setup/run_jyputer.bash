#!/bin/bash

rm /tmp/jnotebook.log; 
jupyter notebook --ip='*'  >& /tmp/jnotebook.log & 
