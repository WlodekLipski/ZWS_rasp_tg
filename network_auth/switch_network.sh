#!/bin/bash

#user input for SSID

#creating a config file for network
echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev" | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf
echo "update_config=1" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
wpa_passphrase $1 $2 | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
sudo reboot now
