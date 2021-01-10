## Hardware Monitor Display - Pi Server

Read CPU and GPU temperature readings from a Windows PC, then display them as a set of gauges on an external display connected to a Raspberry Pi.

This is the set of python scripts that runs on the Pi. For the windows client see this repository: https://github.com/aliktb/Hardware-Monitor-Display-PC-Client


-----

### Requirements

1. Visual Studio 2017 or 2019 with latest update
2. Windows 10 (admin account) with .Net Framework 4.6.2
3. Raspberry Pi (tested with model 3B+ but should work with any variant) with Micro SD card and monitor
4. ethernet cable and optional USB to ethernet dongle if no spare ethernet is available on PC


### Usage

1. Download a fresh copy of Raspbian and install to micro SD (any Pi) or USB (only works on Pi 4)
2. Configure static IP as `190.160.1.5` (not like the common subnet of 192.168.xxx.xxx)
3. Place python files in a new directory in the user's home directory eg. Documents, Downloads etc.
4. Append the following line at the end of the file:
    `@/usr/bin/python3 /home/USER/DIRECTORY_OF_PYTHON_FILES/main.py`
5. Connect Pi to PC via ethernet cable. Can be done with PC motherboard's LAN input or USB to ethernet dongle
6. Connect monitor to Pi vid HDMI. (Currently works with resolution of 1280 x 720)
7. Restart the Pi

### Credits

Temperature data obtained from [Open Hardware Monitor](https://github.com/openhardwaremonitor/openhardwaremonitor)'s `OpenHardwareMonitorLib`


Inspiration and original code: https://github.com/logchan/open-hardware-monitor-arduino

Forked from: https://github.com/octal-ip/open-hardware-monitor-arduino
