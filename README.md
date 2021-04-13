Raspberry Pi Sous Vide
======================

A set of scripts to control the temperature of a water bath for Sous Vide cooking.

Hardware
--------

A slow cooker or rice cooker (or anything else that has a heating element and that can hold the stuff you want to cook and enough water to submerge it)

A 434MHz remote controlled mains socket such as:

[Lloytron A1210WH](https://smile.amazon.co.uk/Lloytron-A1210WH-Remote-Controlled-Socket/dp/B0053XRZ9I)  

I was originally using a socket from [Maplin](https://web.archive.org/web/20120201112313/http://www.maplin.co.uk/additional-remote-controlled-mains-socket-531560),
but they're no longer in business, and that type of socket is impossible to come by these days.

A 434MHz RF transmitter such as:

http://proto-pic.co.uk/434mhz-rf-link-transmitter/

A waterproof DS18B20 temperature sensor (from eBay) and a 4k7 pull up resistor.

I used a [Ciseco Slice of Pi](http://shop.ciseco.co.uk/slice-of-pi-add-on-for-raspberry-pi/) to keep everything tidy, but they're also out of business now :(

Installation
------------

Starting with Raspbian. First make sure that everything is up to date:

    sudo apt-get update && sudo apt-get upgrade -y
    
Install dependencies:

    sudo apt-get install -y git-core screen
    
[Install PiLight](https://manual.pilight.org/installation.html)  
I've added a copy of my /etc/pilight/config.json here.
    
Install these scripts:

    cd~
    git clone https://github.com/cpswan/RPi_sousvide
    
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

![](https://web.archive.org/web/20141024172626if_/http://pi4j.com/images/p1header-large.png)

Before you start
----------------

Take a look in /sys/bus/w1/devices/ to find the device ID for the DS18B20 (e.g. 28-000003ea0350).

Edit 3biased.py and t1.sh with nano/vi or whatever to have the correct ID.

Running
-------

It's a good idea to run this in a screen session:

    screen
    
Optional - have a separate process monitoring temperature, so that there's a log afterwards:

    ./templog.sh &
    tail -f temp_log

Press `ctrl-a c` to create another screen session (`ctrl-a 0` and `ctrl-a 1` can then be used to switch between sessions).
    
The main script will default to 55C:

    ./3biased.py
    
But it can be overridden to cook at different temperatures:

    ./3biased.py -t 60
    
It's also possible to change the control loop variables with command line switches to tune the script to a given cooker.


Disclaimer
----------

This works for me, if you try it yourself and break your Raspberry Pi, ruin your food, or burn down your kitchen then I'm sorry, but it's your problem not mine.
