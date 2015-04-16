#!/bin/bash

runpid=`pgrep -f main.py`
kill $runpid
