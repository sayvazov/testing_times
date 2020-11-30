#!/bin/bash
cd $HOME/Desktop/testing-timer/testing_times
python3 testing-timer.py
git add *
git commit -m "Auto commit"
git push origin main
