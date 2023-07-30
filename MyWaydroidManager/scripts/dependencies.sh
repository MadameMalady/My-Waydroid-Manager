#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   sudo apt install libnotify-bin
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'ubuntu' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   sudo apt install libnotify-bin
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'manjaro' ]; then
   sudo pacman -Sy libnotify
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "to be filled" 
else
   echo "Error 404"
   sleep 3
fi
