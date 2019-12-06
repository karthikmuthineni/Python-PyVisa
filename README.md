# Python-PyVisa
Reading data from Data Acquistion Unit (Model: Keysight 34972A/DAQ970A) using PyVisa and Raspberrypi.

Install PyVisa on Raspberry Pi:
pip install PyVISA

Give USB permission after connecting Raspberry Pi to DAQ using USB-Cable.

Identify the vendorID and productID of your USB device with:
lsusb -vvv

From the lsusb output, find your USB device's entry, and look for "idVendor" and "idProduct" fields. Next, create a new udev rule as follows:
sudo vi /etc/udev/rules.d/50-myusb.rules

Replace "idVendor" and "idProduct" values with your own.

Now reboot your machine or reload udev rules:
sudo udevadm control --reload 


USB Permissions SOURCE:
http://ask.xmodulo.com/change-usb-device-permission-linux.html


