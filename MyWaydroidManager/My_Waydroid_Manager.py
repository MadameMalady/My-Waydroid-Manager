#!/usr/bin/env python3                                                                            

# v 0.1.9
# © 2023 GPL 3.0


import subprocess
import sys
import gi
import os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib

  # Main Application Window:
  

        
class MainWindow(Gtk.ApplicationWindow):
    # Declare current_dir as a class attribute
    current_dir = os.getcwd()


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
            
    # Button 6 Label= 'Install Dependencies':
            
            self.button6 = Gtk.Button(label="Install Dependencies")
            self.box2.append(self.button6)
            
    # Button 6, button size:
            
            self.button6.set_margin_top(250)
            self.button6.set_margin_bottom(20)
            self.button6.set_margin_start(10)
            self.button6.set_margin_end(10)
            
    # Button 6, Function, ' Install_Dependencies ':       
            
            self.button6.connect('clicked', self.Install_Dependencies)
            
            
    # Button 11 Label= 'Install Application':
            
            self.button11 = Gtk.Button(label="Install Application")
            self.box2.append(self.button11)
            
    # Button 11, button size:
            
            self.button11.set_margin_top(10)
            self.button11.set_margin_bottom(20)
            self.button11.set_margin_start(10)
            self.button11.set_margin_end(10)
            
    # Button 11, Function, ' Install_Application ':       
            
            self.button11.connect('clicked', self.Install_Application)
            
            
            
            
            
  # Install Waydroid Window's Button's Definitions:
        
  # Button 2, Main Application Window, Function = Open a new window.
        
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
            
            
            
    # Button 7 Label= 'Purge Waydroid Installation':
        
            self.button7 = Gtk.Button(label="Purge Waydroid Installation")
            self.box3.append(self.button7)
            
    # Button 7, button size:
            
            self.button7.set_margin_top(250)
            self.button7.set_margin_bottom(20)
            self.button7.set_margin_start(10)
            self.button7.set_margin_end(10)
            
    # Button 7, Function, ' Purge_Waydroid_Installation ':       
            
            self.button7.connect('clicked', self.Purge_Waydroid_Installation)
            
            
            
    # Button 9 Label= 'Purge Waydroid Images':
    
    
            self.button9 = Gtk.Button(label="Purge Waydroid Images")
            self.box3.append(self.button9)
            
            
    # Button 9, button size:
            
            self.button9.set_margin_top(10)
            self.button9.set_margin_bottom(20)
            self.button9.set_margin_start(10)
            self.button9.set_margin_end(10)
            
    # Button 9, Function, ' Purge_Waydroid_Images ':       
            
            self.button9.connect('clicked', self.Purge_Waydroid_Images)
            
            
            
            # Ninth button, second window, 'Install Waydroid'
            
            self.button9 = Gtk.Button(label="Install Waydroid")
            self.box3.append(self.button9)
            self.button9.set_margin_top(10)
            self.button9.set_margin_bottom(20)
            self.button9.set_margin_start(10)
            self.button9.set_margin_end(10)
            self.button9.connect('clicked', self.Install_Waydroid)

     # main application window, popover menu, about window
    def show_about(self, action, param):
       
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Kharra Oswin"])
        self.about.set_copyright("© 2023 Kharra Oswin")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://github.com/MadameMalady/My-Waydroid-Manager")
        self.about.set_website_label("Github")
        self.about.set_version("0.1.9")
        self.about.set_logo_icon_name("app.Keo.MyWaydroidManager")  

        self.about.set_visible(True)       
            
#-----------------------------------------------------------------------------------------------------
           
    # This is where we will define what each button Does, and connect a function to each of them.
    
    #Button 3  
    def Advanced_Options(self, button):
        print("here's some more text, developer.")
    
    #Button 6
    def Install_Dependencies(self, button):
        # install dependencies for Waydroid
        print("Installing Dependencies, please wait...")
        #os.system("cd scripts && ./dependencies.sh")
        print(subprocess.run([os.path.join(self.current_dir, 'scripts', "dependencies.sh")], check=True))
        
        
        
    def Install_Application(self,button):
        # install files locally as an application
        print("This will install all the required files locally, in the future you may launch from the app's icon")
        #os.system(f"cd {os.path.join(self.current_dir, 'scripts')} && ./install_application.sh")
        print(subprocess.run([os.path.join(self.current_dir, 'scripts', "install_application.sh")], check=True))
            
    #Button 7
    def Purge_Waydroid_Installation(self, button):
        # Purge Waydroid Installation
        print("This will completely remove waydroid")
        #os.system(f"cd {os.path.join(self.current_dir, 'scripts')} && ./purge.sh")
        print(subprocess.run([os.path.join(self.current_dir, 'scripts', "purge.sh")], check=True))
      
    #Button 9
    def Purge_Waydroid_Images(self, button):
        # Purge Waydroid Images
        print("This will delete all waydroid images and directories")
        #os.system(f"cd {os.path.join(self.current_dir, 'scripts')} && ./purge_images.sh")
        print(subprocess.run([os.path.join(self.current_dir, 'scripts', "purge_images.sh")], check=True))
        
    #Button 9
    def Install_Waydroid(self, button):
        # run 'build.sh' to try and build or install waydroid
        print("Installing Waydroid, please wait..")
        #os.system(f"cd {os.path.join(self.current_dir, 'scripts')} && ./build.sh")
        print(subprocess.run([os.path.join(self.current_dir, 'scripts', "build.sh")], check=True))
        

#-----------------------------------------------------------------------------------------------------

# This tells the app how to open Various Windows, And close them.
    
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
        
            #Button 8
    def Go_Back(self, button):
        # Go back ot the previous Window
        print("going back!")
        self.win = MainWindow(application=app)
        self.win.present()
        
# These lines tell the app what window to open when the app is launched
        
class MyWaydroidManager(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyWaydroidManager(application_id="app.Keo.MyWaydroidManager")
app.run(sys.argv)
