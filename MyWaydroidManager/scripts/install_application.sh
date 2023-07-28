#!/bin/bash

user="$(whoami)"

if [ $(hostname) = 'mobian' ]; then
   
   notify-send "My Waydroid Manager" "Check Your Terminal"
   
   # copy application directory
   mkdir -p /home/$user/MyWaydroidManager
   cp My_Waydroid_Manager.py /home/$user/MyWaydroidManager
   cp -r icons /home/$user/MyWaydroidManager
   cd icons
   sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons/hicolor/scalable/apps
   cp -p app.Keo.MyWaydroidManager.svg ~/.local/share/icons
   sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons
   cd ..
   cp -r scripts /home/$user/MyWaydroidManager
   cd  ~/.local/share/applications 
   touch MyWaydroidManager.desktop
   echo "
[Desktop Entry]
Version=0.1.9
Name=My Waydroid Manager
Comment=Manage Waydroid installations easily
Exec=/usr/bin/env python3 /home/$user/MyWaydroidManager/My_Waydroid_Manager.py
Icon=/home/$user/MyWaydroidManager/icons/app.Keo.MyWaydroidManager.svg
X-Purism-FormFactor=Workstation;Mobile;
Terminal=true
Type=Application">MyWaydroidManager.desktop
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'ubuntu' ]; then
   
   notify-send "My Waydroid Manager" "Check Your Terminal"
   
   # copy application directory
   mkdir -p /home/$user/MyWaydroidManager
   cp My_Waydroid_Manager.py /home/$user/MyWaydroidManager
   cp -r icons /home/$user/MyWaydroidManager
   cd icons
   sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons/hicolor/scalable/apps
   cp -p app.Keo.MyWaydroidManager.svg ~/.local/share/icons
   sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons
   cd ..
   cp -r scripts /home/$user/MyWaydroidManager
   cd  ~/.local/share/applications 
   touch MyWaydroidManager.desktop
   echo "
[Desktop Entry]
Version=0.1.9
Name=My Waydroid Manager
Comment=Manage Waydroid installations easily
Exec=/usr/bin/env python3 /home/$user/MyWaydroidManager/My_Waydroid_Manager.py
Icon=/home/$user/MyWaydroidManager/icons/app.Keo.MyWaydroidManager.svg
X-Purism-FormFactor=Workstation;Mobile;
Terminal=true
Type=Application">MyWaydroidManager.desktop
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'manjaro' ]; then
   echo "to be filled"
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "to be filled" 
else
   echo "Error 404"
   sleep 3
fi

