#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   sudo apt install curl ca-certificates -y
   curl https://repo.waydro.id | sudo bash
   sudo apt install waydroid -y
   echo "Please Launch waydroid from it's application icon, minimize osk"
elif [ $(hostname) = 'ubuntu' ]; then
   sudo apt install curl ca-certificates -y
   curl https://repo.waydro.id | sudo bash
   sudo apt install waydroid -y
   echo "Please Launch waydroid from it's application icon, minimize osk"
elif [ $(hostname) = 'manjaro' ]; then
   sudo pacman -Syyu waydroid
   waydroid
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "Sorry, this option's still a work in progress"
else
   echo "Error 404"
fi
