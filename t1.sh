#!/bin/bash
# replace 28-000003ea0350 below with the address for your DS18B20
cat /sys/bus/w1/devices/28-000003ea0350/w1_slave | grep t= | sed s/.*t=//
