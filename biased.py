#!/usr/bin/python
import os
from subprocess import Popen, PIPE, call
from optparse import OptionParser
from time import sleep

def tempdata():
    # Replace 28-000004ce4a45 with the address of your DS18B20
    pipe = Popen(["cat","/sys/bus/w1/devices/w1_bus_master1/28-000004ce4a45/w1_slave"], stdout=PIPE)
    result = pipe.communicate()[0]
    result_list = result.split("=")
    temp_mC = int(result_list[-1]) # temp in milliCelcius
    return temp_mC

def setup_1wire():
  os.system("sudo modprobe w1-gpio && sudo modprobe w1-therm")

def setup_pilight() :
  os.system("sudo service pilight start")

def turn_on():
  os.system("sudo ./on.sh")

def turn_off():
  os.system("sudo ./off.sh") 

#Get command line options
parser = OptionParser()
parser.add_option("-t", "--target", type = int, default = 55)
parser.add_option("-p", "--prop", type = int, default = 6)
parser.add_option("-i", "--integral", type = int, default = 2)
parser.add_option("-b", "--bias", type = int, default = 22)
(options, args) = parser.parse_args()
target = options.target * 1000
print ('Target temp is %d' % (options.target))
P = options.prop
I = options.integral
B = options.bias
# Initialise some variables for the control loop
interror = 0
pwr_cnt=1
pwr_tot=0
# Setup 1Wire for DS18B20
#setup_1wire()
# Setup pilight
setup_pilight()
# Turn on for initial ramp up
state="on"
turn_on()

temperature=tempdata()
print("Initial temperature ramp up")
while (target - temperature > 6000):
    sleep(15)
    temperature=tempdata()
    print(temperature)

print("Entering control loop")
while True:
    temperature=tempdata()
    print(temperature)
    error = target - temperature
    interror = interror + error
    power = B + ((P * error) + ((I * interror)/100))/100
    print power
    if (power > 0):
        pwr_tot = pwr_tot + power
    pwr_ave = pwr_tot / pwr_cnt
    pwr_cnt = pwr_cnt + 1
    print pwr_ave
    # Make sure that if we should be off then we are
    if (state=="off"):
        turn_off()
    else:
        turn_on()
    # Long duration pulse width modulation
    for x in range (1, 100):
        if (power > x):
            if (state=="off"):
                state="on"
                print("On")
                turn_on()
        else:
            if (state=="on"):
                state="off"
                print("Off")
                turn_off()
        sleep(1)
