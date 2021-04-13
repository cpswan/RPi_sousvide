#!/bin/bash
#script to log temperature every 15 seconds
#usage: ./temploop.sh &
#then: tail -f temp_log
#best run in a screen (sudo apt-get screen if not installed)
while :
do
  ./t1.sh >> temp_log
  sleep 15
done
