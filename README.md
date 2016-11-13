# raspberrypi-radio

This project aims at giving a web layer to the piradio project:
http://www.dronkert.net/rpi/radio.html

# Prerequisites
* Apache with PHP5 https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md
* MPC / MPD https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen/installing-the-music-player-daemon

Install

```shell
sudo ln -s ~/raspberrypi-webradio/bin/piradio /usr/local/bin/piradio
sudo chmod 755 /usr/local/bin/piradio
sudo ln -s ~/raspberrypi-webradio/web/ /var/www/radio
```

Other useful references
https://www.internet-radio.com/


