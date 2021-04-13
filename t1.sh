#!/bin/bash
cat /sys/bus/w1/devices/28-000004ce4a45/w1_slave | grep t= | sed s/.*t=//
