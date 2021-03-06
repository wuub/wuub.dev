title: Completely wireless setup for your drone racing simulator 
date: 2019-05-19 12:00
tags: fpv, electronics
slug: sim-wireless-setup
description: You want to play your favorite simulator using standard transmitter and goggles? USB and HDMI cables make everything feel heavy and constraint? This post is for you.
status: published


{% img images/wireless-fpv/cover.jpg %}


## Simulators

There are several notable simulators on the market, namely [VelociDrone](https://www.velocidrone.com/),  [DRL Sim](https://thedroneracingleague.com/drl-sim-3/) and [Liftoff](https://www.liftoff-game.com/).

Setup described in this post is universal and works with all of them, but since Liftoff is my sim of choice
I'll use it as an example :)


## The Problem

We keep our gaming PC in the living room. It makes sense: 4K TV, surround sound, comfortable couch.  

What doesn't make any sense is running **5m+ USB cable** from PC to the transmitter and a
**5m+ HDMI** cable to the goggles to get an immersive simulator experience.

With a few cheap components and basic soldering I was able to go completely wireless.
Let me show you how.

But first here's a **Fatshark DVR** of the finished product (keep in mind that video looks order of magnitude better 
in the goggles during play)

{% youtube 7f8tGgE05uY %}


## Making the transmitter wireless [sic!]

Did you know that you can use your transmitter to control things over long distances
without any wires? Shocking, right? :)  


### off-the-shelf solution

With FrSky, the easiest way to ditch the USB cable is to just buy a [XSR-SIM](https://www.frsky-rc.com/product/xsr-sim/). 
No firmware flashing, no soldering, printing enclosures, etc. Plug it into your PC, bind with a new model and fly. 
It works just like any 2.4GHz D16 receiver on your quad. 

{% img images/wireless-fpv/dongle.jpg %}

It's a bit on the pricey side but performs flawlessly. Just make sure that your firmware versions match (FCC vs EU-LBT). 

### diy

Alternatively if you use FlySky/Spectrum or don't want to spend extra money and have a spare F4/F7 flight controller and unused receiver, you might be interested in using Betaflight's [USB HID joystick mode](https://github.com/betaflight/betaflight/wiki/HID-Joystick-Support).
It can transform any receiver into USB joystick which can be used to fly a simulator. 

JB can show you [how](https://www.youtube.com/watch?v=wuobzowLfj0) some flashing is required, but if you know how to configure
Betaflight you'll be fine.


## Making your goggles wireless [duh!]

{% img images/wireless-fpv/goggles.jpg %}


Surprisingly, your goggles are also capable of working without wires (can you notice the antennas) :) And just like in the case of 2.4GHz signal, there are two options. 

### off-the-shelf solution

You could probably buy something like [Skyzone TX-5D](https://www.getfpv.com/skyzone-tx-5d-5-8ghz-32ch-600mw-av-transmitter-w-hdmi-port.html) and connect it to your PC's HDMI port. 
I have not tried doing this, but it should work, at least in theory. 600mW output power
might be an issue though (heat, power consumption, multipathing, causing interference in residential area)


### diy

We can use quad components to build HDMI capable video link. 

All we need is any standard **5.8GHz VTX** and a **HDMI to AV** converter. Since most VTXes are designed
for in flight operation (cooling) we should add **a fan** to prevent overheating. 

Specifically:

- [Mini HDMI2AV](https://www.banggood.com/Onten-OTN-7336B-HDMI-to-AV-Audio-Converter-for-DVD-Laptop-PC-p-1331698.html) ~9$
- [Eachine VTX03](https://www.banggood.com/Eachine-VTX03-Super-Mini-5_8G-72CH-025mW50mw200mW-Switchable-FPV-Transmitter-p-1114206.html) because I had it lying around and it can be switched down to 25mW, buy a [VTX01](https://www.banggood.com/Eachine-VTX01-Super-Mini-5_8G-40CH-25mW-FPV-Transmitter-p-1114203.html) if it's cheaper. ~8$  
- [40x40 5V Fan](http://www.aliexpress.com/item/1-PC-5V-0-14A-40MM-4CM-40-40-10mm-4010-DC-CPU-Brushless-Cooling-Cooler/32698690076.html) not this exact one, but this size ~2$


To perform this simple mod open the plastic shell of HDMI2AV. 

Strip some insulation from the end of black/red wire pairs of the VTX and the cooling fan
(leave black/red/yellow alone for now). Join red wires (PWR) together and
carefully solder them to this point on the PCB.

{% img images/wireless-fpv/pcb-5v.png %}

As far as I can tell this is the only place where raw USB 5V is easily accessible.

Black (GND) wires can be soldered to any GND terminals. USB port's case or any of its side legs are good choices. 
They are far from other components and difficult to damage.

Now cut off the connector from black/red/yellow bundle. Strip some insulation off yellow (video) and black (gnd) 
wires and solder them to correct terminals. Bottom of the PCB is a good option, there's video signal on the top as well 
(vertical metal prong in the AV connector) if you prefer.

{% img images/wireless-fpv/video.jpg %}

#### Test time

Plug in USB power. If you're using power-switchable VTX set it to **25mW**. Pick a channel (after closing the box
access to the VTX will be limited).
Now turn on your goggles and see if everything works. Your should see a test image like this one:


{% img images/wireless-fpv/ok.png %}


#### Finishing touches 

Now take the top half of HDMI2AV and cut a hole in it for the fan (a knife and small pliers are good enough 
for the job, use eye protection because the plastic breaks easily). Make the hole large enough for
the air to freely **blow into** the case, but small enough that you can tape down the fan corners..

Use double sided tape to mount the fan and the VTX as shown in the picture below.
VTX is floating freely just below the fan, airflow is keeping it cool. 

{% img images/wireless-fpv/fan.jpg %}

DO NOT mount the VTX on the HDMI2AV PCB. Many of its components get very hot during operation, not to mention
accidental short circuits.

Now carefully close the lid taking care to not pinch any wires. 

{% img images/wireless-fpv/complete.jpg %}


#### Connecting to the PC

Connect both HDMI and USB cables to your PC. 
Either extend (you'll need to choose correct display in Liftoff) or duplicate you display.
Choose reasonable resolution for HDMI2AV (1280x720 seems to work well)
Start Liftoff and enjoy :)

## Notes and disclaimers

 - You're broadcasting your screen unencrypted for all your neighbors to see.  Don't read private emails while VTX is enabled.
 - I tested HDMI2AV + VTX continuously for over an hour and it seems to keep stable temperature.
 - The same cannot be said about Fatshark HDOs + Pro58 receiver. The heat seems to spread and I prefer to let the goggles cool every 20 minutes or so. 