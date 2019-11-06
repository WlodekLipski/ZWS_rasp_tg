
#!/bin/sh

working_dir="/home/pi/ZWS_rasp_tg/"
sudo service wpa_supplicant restart
sudo wpa_supplicant -D wext -i wlan0  -c /etc/wpa_supplicant/wpa_supplicant.conf -B
WPA_PID=$!
sleep 2
sudo dhclient -1
if [ $? -eq 0 ]
then
	echo "Connected"
	cd $working_dir && python3 ./Telegram_Bot/rasp_bot.py &
	cd $working_dir && python3 ./Web_app/app.py &
else
	echo "No internet"
	sudo kill $WPA_PID
	sudo service wpa_supplicant stop
	sudo iptables-restore /etc/iptables.ipv4.nat
	sudo ifup wlan0
	sudo service hostapd start
	sudo service dnsmasq start
	cd $working_dir && python ./network_auth/app.py
fi
