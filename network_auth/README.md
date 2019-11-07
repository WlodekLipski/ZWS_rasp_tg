This is a simple single-page application. It will run if RPi enables its hotspot.

![img](https://i.ibb.co/C9XyPx5/img.png)

The goal of this app is to get private network credentials from the user. And connect RPi to this network.

After the user enters the SSID and password of the network, the credentials will be validated. SSID must be shorter than 32 characters and the password's length must be between 8 and 32 characters. If credentials are valid user will be able to confirm them.
After that wpa_supplicant.conf will be updated and RPi will reboot.
On startup, RPi will try to connect to the network using credentials from wpa_supplicant.conf. If it does not succeed, RPi will enable its hotspot and run this app once again.