#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   sudo apt install curl ca-certificates -y
   curl https://repo.waydro.id | sudo bash
   sudo apt install waydroid -y
   notify-send "My Waydroid Manager" "Launch Waydroid from it's application icon, minimize osk"
   sleep 3
   exit
elif [ $(hostname) = 'ubuntu' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   sudo apt install curl ca-certificates -y
   curl https://repo.waydro.id | sudo bash
   sudo apt install waydroid -y
   notify-send "My Waydroid Manager" "Launch Waydroid from it's application icon, minimize osk"
   sleep 3
   exit
elif [ $(hostname) = 'manjaro' ]; then
   sudo pacman -Syyu waydroid
   waydroid
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "Sorry, this option's still a work in progress"
else
   echo "Error 404"
   sleep 3
   exit
fi

