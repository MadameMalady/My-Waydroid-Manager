#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   waydroid session stop
   sudo waydroid container stop
   sudo apt remove waydroid
   exit
elif [ $(hostname) = 'ubuntu' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   waydroid session stop
   sudo waydroid container stop
   sudo apt remove waydroid
   exit
elif [ $(hostname) = 'manjaro' ]; then
   echo "to be filled"
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "to be filled" 
else
   echo "Error 404"
   sleep 3
   exit
fi
