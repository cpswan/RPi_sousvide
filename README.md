Raspberry Pi Sous Vide
======================

A set of scripts to control the temperature of a water bath for Sous Vide cooking.

Hardware
--------

A slow cooker or rice cooker (or anything else that has a heating element and that can hold the stuff you want to cook and enough water to submerge it)

A 434MHz remote controlled mains socket such as:

http://www.maplin.co.uk/additional-remote-controlled-mains-socket-531560

A 434MHz RF transmitter such as:

http://proto-pic.co.uk/434mhz-rf-link-transmitter/

A waterproof DS18B20 temperature sensor (from eBay) and a 4k7 pull up resistor.

Optional - a Ciseco Slice of Pi to keep everything tidy:

http://shop.ciseco.co.uk/slice-of-pi-add-on-for-raspberry-pi/

Installation
------------

Starting with Raspbian "wheezy". First make sure that everything is up to date:

    sudo apt-get update && sudo apt-get upgrade -y
    
Install dependencies:

    sudo apt-get install -y git-core python2.7-dev python-setuptools screen
    
Install WiringPi (I'm not sure that WiringPi Python needs this first, but it didn't work without when I tried):

    cd ~
    git clone git://git.drogon.net/wiringPi
    cd wiringPi
    ./build
    
Install WiringPi Python:

    cd ~
    git clone https://github.com/WiringPi/WiringPi-Python.git
    cd WiringPi-Python/
    git submodule update --init
    sudo python setup.py install
    
Optional - install the full raspberry-stroganoff that this is based on (key files are already in this repo):

    cd ~
    git clone https://github.com/dmcg/raspberry-strogonanoff
    
Install these scripts:

    cd~
    git clone https://github.com/cpswan/RasPi/SousVide
    
Circuit
-------

The 434MHz receiver needs to be connected like this:

<table>
<tr><th>Tx Pin</th><th>Raspberry Pi Header Pin</th></tr>
<tr><td>Pin 1 GND</td><td>Pin 6 0V (Ground)</td></tr> 
<tr><td>Pin 2 Data in</td><td>Pin 11 GPIO 0</td></tr> 
<tr><td>Pin 3 Vcc</td><td>Pin 2 5.0 VDC Power</td></tr> 
<tr><td>Pin 4 ANT</td><td>173mm antenna wire (not on the Pi!)</td></tr> 
</table>

and the DS18B20 needs to be connected like this:

<table>
<tr><th>Tx Pin</th><th>Raspberry Pi Header Pin</th></tr>
<tr><td>Black</td><td>Pin 6 0V (Ground)</td></tr> 
<tr><td>White</td><td>Pin 7 GPIO 7</td></tr> 
<tr><td>Red</td><td>Pin 1 3.3 VDC Power</td></tr> 
</table>

Here's a reminder of the Raspberry Pi GPIO pinout:

![](http://pi4j.com/images/p1header-large.png)

Running
-------

It's a good idea to run this in a screen session:

    screen
    
Optional - have a separate process monitoring temperature, so that there's a log afterwards:

    cd SousVide
    ./templog.sh &
    tail -f temp_log
    
The main script will default to 55C:

    python ./sousvide.py
    
But it can be overridden to cook at different temperatures:

    python ./sousvide.py -t 60
    
It's also possible to change the control loop variables with command line switches to tune the script to a given cooker.


Disclaimer
----------

This works for me, if you try it yourself and break your Raspberry Pi, ruin your food, or burn down your kitchen then I'm sorry, but it's your problem not mine.