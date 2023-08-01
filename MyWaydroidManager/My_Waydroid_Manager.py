#!/usr/bin/env python3                                                                            

# v 0.2.1
# © 2023 GPL 3.0


import subprocess
import sys
import gi
import os
#import contextlib
#import io
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib

  # Main Application Window:
  

        
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        
        #set app name w/ GLib
        GLib.set_application_name("My Waydroid Manager")

        # Create a new "Action"
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)

        # 'About' action menu
        menu = Gio.Menu.new()
        menu.append("About", "win.about")  

        # Create a popover
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")

        # Add menu button to the header bar
        self.header.pack_end(self.hamburger)
                
        # Main Application window size:      
        
        self.set_default_size(360, 720)
        
        # Main Application window Title:        
        
        self.set_title("My Waydroid Manager")
        
        # Main Application window, Box 1:
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        
        # Button 1 Label= 'First Time Setup':
       
        self.button1 = Gtk.Button(label="First-time Setup")
        self.box1.append(self.button1)
        
        # Button 1, button size:
        
        self.button1.set_margin_top(250)
        self.button1.set_margin_bottom(20)
        self.button1.set_margin_start(10)
        self.button1.set_margin_end(10)
        
        # Button 1, Function, ' First_Time_Setup ':       
        
        self.button1.connect('clicked', self.First_Time_Setup)

        
        # Button 2 Label= 'Manage Install'
        
        self.button2 = Gtk.Button(label="Manage Install")
        self.box1.append(self.button2)
        
        # Button 2, button size:
        
        self.button2.set_margin_top(10)
        self.button2.set_margin_bottom(20)
        self.button2.set_margin_start(10)
        self.button2.set_margin_end(10)
        
        # Button 2, Function, ' First_Time_Setup ':       
        
        self.button2.connect('clicked', self.Manage_Install)
        
        
    # Main Application Window's Button's Definitions:
        
    # Button 1, Main Application Window, Function = Open a new window.
    
    # Button 1 def:
        
    def First_Time_Setup(self, button):

        # First Time Setup Window:
    
        class FirstTimeSetupWindow(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
            
            
            # Header Bar, left side, back button
            
            self.Back_Button = Gtk.Button(label="Back")
            self.header.pack_start(self.Back_Button)
            self.Back_Button.set_icon_name("go-previous-symbolic")
            
            # Left side of header bar, 'Back_Button' function:
             
            self.Back_Button.connect('clicked', self.Go_Back)
            
            # First Time Setup window size:      
    
            self.set_default_size(360, 720)
            
            # First Time Setup window Title:
            
            self.set_title("My Waydroid Manager")
            
            # First Time Setup window, Box 2:
        
            self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box2)
            
            # Button 3 Label= 'Install Dependencies':
            
            self.button3 = Gtk.Button(label="Install Dependencies")
            self.box2.append(self.button3)
            
            # Button 3, button size:
            
            self.button3.set_margin_top(250)
            self.button3.set_margin_bottom(20)
            self.button3.set_margin_start(10)
            self.button3.set_margin_end(10)
            
            # Button 3, Function, ' Install_Dependencies ':       
            
            self.button3.connect('clicked', self.Install_Dependencies)
            
            
            # Button 4 Label= 'Install Application':
            
            self.button4 = Gtk.Button(label="Install Application")
            self.box2.append(self.button4)
            
            # Button 4, button size:
            
            self.button4.set_margin_top(10)
            self.button4.set_margin_bottom(20)
            self.button4.set_margin_start(10)
            self.button4.set_margin_end(10)
            
            # Button 4, Function, ' Install_Application ':       
            
            self.button4.connect('clicked', self.Install_Application)
            
            
    # Install Waydroid Window's Button's Definitions:
        
    # Button 2 def:
        
    def Manage_Install(self, button):
        # create a second application window to be called by a button from the primary application window.
 
        class Manage_Install(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
            
            
            # Header Bar, left side, back button
            
            self.Back_Button = Gtk.Button(label="Back")
            self.header.pack_start(self.Back_Button)
            self.Back_Button.set_icon_name("go-previous-symbolic")
            
            
            # Left side of header bar, 'Back_Button' function:
            
            self.Back_Button.connect('clicked', self.Go_Back)            
    
            self.set_default_size(360, 720)
            self.set_title("My Waydroid Manager")
            
            # Third Box, needed to put buttons inside of.
        
            self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box3)
            
            # Button 5 Label= 'Purge Waydroid Installation':
        
            self.button5 = Gtk.Button(label="Purge Waydroid Installation")
            self.box3.append(self.button5)
            
            # Button 5, button size:
            
            self.button5.set_margin_top(230)
            self.button5.set_margin_bottom(20)
            self.button5.set_margin_start(10)
            self.button5.set_margin_end(10)
            
            # Button 5, Function, ' Purge_Waydroid_Installation ':       
            
            self.button5.connect('clicked', self.Purge_Waydroid_Installation)
            
            # Button 6 Label= 'Purge Waydroid Images':
    
    
            self.button6 = Gtk.Button(label="Purge Waydroid Images")
            self.box3.append(self.button6)
            
            # Button 6, button size:
            
            self.button6.set_margin_top(10)
            self.button6.set_margin_bottom(20)
            self.button6.set_margin_start(10)
            self.button6.set_margin_end(10)
            
            # Button 6, Function, ' Purge_Waydroid_Images ':       
            
            self.button6.connect('clicked', self.Purge_Waydroid_Images)
            
            # Button 7 Label= 'Install Waydroid':
            
            self.button7 = Gtk.Button(label="Install Waydroid")
            self.box3.append(self.button7)
            
            # Button 7, button size:
            
            self.button7.set_margin_top(10)
            self.button7.set_margin_bottom(20)
            self.button7.set_margin_start(10)
            self.button7.set_margin_end(10)
            
            # Button 7, Function, ' Install_Waydroid ':       
            
            self.button7.connect('clicked', self.Install_Waydroid)
            
            # Button 8 Label= 'Google Play Certification':
    
            self.button8 = Gtk.Button(label="Google Play Certification")
            self.box3.append(self.button8)
                    
            # Button 8, button size:
            
            self.button8.set_margin_top(10)
            self.button8.set_margin_bottom(20)
            self.button8.set_margin_start(10)
            self.button8.set_margin_end(10)
            
            # Button 8, Function, ' Get_Registration_Code ':       
            
            self.button8.connect('clicked', self.Get_Registration_Code)

    # main application window, popover menu, about window
    def show_about(self, action, param):
       
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Kharra Oswin, RobetofLocksley"])
        self.about.set_copyright("© 2023 GPL 3.0")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://github.com/MadameMalady/My-Waydroid-Manager")
        self.about.set_website_label("Github")
        self.about.set_version("0.2.1")
        self.about.set_logo_icon_name("app.Keo.MyWaydroidManager")  

        self.about.set_visible(True)

    # Button 3 def:
    def Install_Dependencies(self, button):
        # Multiline bash code
        dependencies_bash = """
        if [ $(hostname) = 'mobian' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo apt install libnotify-bin
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo apt install libnotify-bin
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
                sudo pacman -Sy libnotify 
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'postmarketos*' ]; then
                echo "to be implemented" 
        else
                echo "Error 404"
                sleep 3
        fi      
        """
        print("Installing Dependencies, please wait...")
        subprocess.run(["bash", "-c", dependencies_bash], check=True)
        
    # Button 4 def:    
    def Install_Application(self,button):
        # Multiline bash code
        install_application_bash = """
        user="$(whoami)"

        if [ $(hostname) = 'mobian' ]; then
                
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                
                # copy application directory
                mkdir -p /home/$user/MyWaydroidManager
                cp My_Waydroid_Manager.py /home/$user/MyWaydroidManager
                cp -r icons /home/$user/MyWaydroidManager
                cd icons
                sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons/hicolor/scalable/apps
                cp -p app.Keo.MyWaydroidManager.svg ~/.local/share/icons
                sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons
                cd symbolic
                sudo cp -p my-waydroid-manager-notify.svg /usr/share/icons/hicolor/scalable/status/
                cd ..
                cd ..
                cd  ~/.local/share/applications 
                touch MyWaydroidManager.desktop
                echo "
        [Desktop Entry]
        Version=0.2.1
        Name=My Waydroid Manager
        Comment=Manage Waydroid installations easily
        Exec=/usr/bin/env python3 /home/$user/MyWaydroidManager/My_Waydroid_Manager.py
        Icon=/home/$user/MyWaydroidManager/icons/app.Keo.MyWaydroidManager.svg
        X-Purism-FormFactor=Workstation;Mobile;
        Terminal=true
        Type=Application">MyWaydroidManager.desktop
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
                
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                
                # copy application directory
                mkdir -p /home/$user/MyWaydroidManager
                cp My_Waydroid_Manager.py /home/$user/MyWaydroidManager
                cp -r icons /home/$user/MyWaydroidManager
                cd icons
                sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons/hicolor/scalable/apps
                cp -p app.Keo.MyWaydroidManager.svg ~/.local/share/icons
                sudo cp -p app.Keo.MyWaydroidManager.svg /usr/share/icons
                cd symbolic
                sudo cp -p my-waydroid-manager-notify.svg /usr/share/icons/hicolor/scalable/status/
                cd ..
                cd ..
                cd  ~/.local/share/applications 
                touch MyWaydroidManager.desktop
                echo "
        [Desktop Entry]
        Version=0.2.1
        Name=My Waydroid Manager
        Comment=Manage Waydroid installations easily
        Exec=/usr/bin/env python3 /home/$user/MyWaydroidManager/My_Waydroid_Manager.py
        Icon=/home/$user/MyWaydroidManager/icons/app.Keo.MyWaydroidManager.svg
        X-Purism-FormFactor=Workstation;Mobile;
        Terminal=true
        Type=Application">MyWaydroidManager.desktop
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
                echo "to be implemented"
        elif [ $(hostname) = 'postmarketos*' ]; then
                echo "to be implemented" 
        else
                echo "Error 404"
                sleep 3
        fi      
        """
        print("This will install all the required files locally, in the future you may launch from the app's icon")
        subprocess.run(["bash", "-c", install_application_bash], check=True)
            
    # Button 5 def:
    def Purge_Waydroid_Installation(self, button):
        # Multiline bash code
        purge_bash = """
        if [ $(hostname) = 'mobian' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                waydroid session stop
                sudo waydroid container stop
                sudo apt remove waydroid -y
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                waydroid session stop
                sudo waydroid container stop
                sudo apt remove waydroid -y
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
                echo "to be implemented"
        elif [ $(hostname) = 'postmarketos*' ]; then
                echo "to be implemented" 
        else
                echo "Error 404"
                sleep 3
        fi      
        """
        print("This will completely remove waydroid")
        subprocess.run(["bash", "-c", purge_bash], check=True)
      
    # Button 6 def:
    def Purge_Waydroid_Images(self, button):
        # Multiline bash code
        purge_images_bash = """
        if [ $(hostname) = 'mobian' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo rm -rf /var/lib/waydroid /home/.waydroid ~/waydroid ~/.share/waydroid ~/.local/share/applications/*aydroid* ~/.local/share/waydroid
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo rm -rf /var/lib/waydroid /home/.waydroid ~/waydroid ~/.share/waydroid ~/.local/share/applications/*aydroid* ~/.local/share/waydroid
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
                echo "to be implemented"
        elif [ $(hostname) = 'postmarketos*' ]; then
                echo "to be implemented" 
        else
                echo "Error 404"
                sleep 3
        fi      
        """
        print("This will delete all waydroid images and directories")
        subprocess.run(["bash", "-c", purge_images_bash], check=True)
        
    #Button 7 def:
    def Install_Waydroid(self, button):
        # Multiline bash code
        build_bash = """
        if [ $(hostname) = 'mobian' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo apt install curl ca-certificates -y
                curl https://repo.waydro.id | sudo bash
                sudo apt install waydroid -y
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "You may now launch Waydroid from its application icon and pick an image type."
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
                sudo apt install curl ca-certificates -y
                curl https://repo.waydro.id | sudo bash
                sudo apt install waydroid -y
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "You may now launch Waydroid from its application icon and pick an image type."
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
                sudo pacman -Syyu waydroid
                waydroid
                notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
                echo "Done!"
        elif [ $(hostname) = 'postmarketos*' ]; then
                echo "Sorry, this option's still a work in progress"
        else
                echo "Error 404"
        fi      
        """
        print("Installing Waydroid, please wait..")
        subprocess.run(["bash", "-c", build_bash], check=True)

    # Button 8 def:
    def Get_Registration_Code(self, button):
        # Multiline bash code
        Retrieve_Registration_Code_bash = """
        if [ $(hostname) = 'mobian' ]; then
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
            read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
            echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
            sleep 3
            touch Registration_Code.txt
            sudo waydroid shell
            ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
            echo "Done!"
        elif [ $(hostname) = 'ubuntu' ]; then
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
            read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
            echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
            sleep 3
            touch Registration_Code.txt
            sudo waydroid shell
            ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
            echo "Done!"
        elif [ $(hostname) = 'manjaro' ]; then
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Please check your Terminal"
            read -p "You need to have ran Waydroid at least once and picked an image type to run this option, If you've not done so yet, please launch Waydroid"
            echo ("Hit ctrl+c to cancel or, wait 3 seconds to continue")
            touch Registration_Code.txt
            sudo waydroid shell
            ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";" > Registration_Code.txt
            notify-send -i /usr/share/icons/hicolor/scalable/status/my-waydroid-manager-notify.svg "My Waydroid Manager" "Done!"
            echo "Done!"
        elif [ $(hostname) = 'postmarketos*' ]; then
            echo "Sorry, this option's still a work in progress"
        else
            echo "Error 404"
        fi      
        """
        print("Installing Waydroid, please wait..")
        subprocess.run(["bash", "-c", Retrieve_Registration_Code_bash], check=True)

    # def on activate:
    
    def on_activate(self, app):
        self.win = FirstTimeSetupWindow(application=app)
        self.win.present()
        FirstTimeSetupWindow = Gtk.ApplicationWindow()
        FirstTimeSetupWindow.connect("destroy", Gtk.ApplicationWindow)
        FirstTimeSetupWindow.show()
        
    def on_activate(self, app):
        self.win = InstallWaydroidWindow(application=app)
        self.win.present()
        InstallWaydroidWindow = Gtk.ApplicationWindow()
        InstallWaydroidWindow.connect("destroy", Gtk.ApplicationWindow)
        InstallWaydroidWindow.show()
        
    def on_destroy(self, widget):
        widget.destroy()
        
    def Go_Back(self, button):
        # Go back ot the previous Window
        print("going back!")
        self.win = MainWindow(application=app)
        self.win.present()
        
# Init defs:
        
class MyWaydroidManager(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyWaydroidManager(application_id="app.Keo.MyWaydroidManager")
app.run(sys.argv)
