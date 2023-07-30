#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
   echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
   sleep 3
   touch Registration_Code.txt
   sudo waydroid shell
   ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'ubuntu' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
   echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
   sleep 3
   touch Registration_Code.txt
   sudo waydroid shell
   ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'manjaro' ]; then
   notify-send "My Waydroid Manager" "Check Your Terminal"
   read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
   echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
   touch Registration_Code.txt
   sudo waydroid shell
   ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
   notify-send "My Waydroid Manager" "Done!"
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "Sorry, this option's still a work in progress"
else
   echo "Error 404"
fi

