#!/usr/bin/env python3

import sys
import gi
import os
import subprocess
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw






# first, create the main window for the application
        
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        
        self.set_default_size(360, 720)
        self.set_title("My Waydroid Manager")
        
        # second, create a box to place buttons inside of
        
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        
        
        # Break-down of these lines:  ' self.button_ ' this is the name of the button, it could be just 'button' or 'button_' where the '_' can be an number.
        # 'Gtk.Button(label="___")' this line is exactly what it looks like, it puts text on your button so you know what it is.
        # 'self.box_.append' the '_' could be any box number, in this case it's box1; and this is telling the prograqm *where* your button gets placed; in this case, it's a little special, as it's the-
        # -first button, it will be 'append'ed to itself! this will put it at the top of the box1 container.
        
        # First Button 'First Time Setup'
       
        #self.button1 = Gtk.Button(label="First-time Setup")
        #self.box1.append(self.button1)
        #self.button1.set_margin_top(200)
        #self.button1.set_margin_bottom(20)
        #self.button1.set_margin_start(10)
        #self.button1.set_margin_end(10)
        #self.button1.connect('clicked', self.First_Time_Setup)

        
        # second button 'Install Waydroid'
        
        self.button2 = Gtk.Button(label="Install Waydroid")
        self.box1.append(self.button2)
        self.button2.set_margin_top(200)
        self.button2.set_margin_bottom(20)
        self.button2.set_margin_start(10)
        self.button2.set_margin_end(10)
        self.button2.connect('clicked', self.Install_Waydroid)
        
        # third button 'Advanced Options'
        
        self.button3 = Gtk.Button(label="Advanced Options")
        self.box1.append(self.button3)
        self.button3.set_margin_top(10)
        self.button3.set_margin_bottom(20)
        self.button3.set_margin_start(10)
        self.button3.set_margin_end(10)
        self.button3.connect('clicked', self.Advanced_Options)
        
        # fourth button 'Help!
        
        self.button4 = Gtk.Button(label="Help!")
        self.box1.append(self.button4)
        self.button4.set_margin_top(10)
        self.button4.set_margin_bottom(20)
        self.button4.set_margin_start(10)
        self.button4.set_margin_end(10)
        self.button4.connect('clicked', self.Help)
        
        # fith button 'About'
        
        self.button5 = Gtk.Button(label="About")
        self.box1.append(self.button5)
        self.button5.set_margin_top(10)
        self.button5.set_margin_bottom(20)
        self.button5.set_margin_start(10)
        self.button5.set_margin_end(10)
        self.button5.connect('clicked', self.About)
        
        # define what each button actually does:
        
    #First Buton, on the main window. Opens a new window.
    
#----------------------------------------------------------------------------------------------------
        
    def First_Time_Setup(self, button):
        # create a second application window to be called by a button from the primary application window.
 
        class FirstTimeSetupWindow(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
    
            self.set_default_size(360, 720)
            self.set_title("My Waydroid Manager")
            
            # Second Box, needed to put buttons inside of.
        
            self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box2)
            
            # sixth button, second window, 'Install Dependencies'
            
            self.button6 = Gtk.Button(label="Install Dependencies")
            self.box2.append(self.button6)
            self.button6.set_margin_top(200)
            self.button6.set_margin_bottom(20)
            self.button6.set_margin_start(10)
            self.button6.set_margin_end(10)
            self.button6.connect('clicked', self.Install_Dependencies)
            
            # Seventh button 'Purge Waydroid Installation' , second window
        
            self.button7 = Gtk.Button(label="Purge Waydroid Installation")
            self.box2.append(self.button7)
            self.button7.set_margin_top(10)
            self.button7.set_margin_bottom(20)
            self.button7.set_margin_start(10)
            self.button7.set_margin_end(10)
            self.button7.connect('clicked', self.Purge_Waydroid_Installation)
        
            # Eighth button 'Go Back' , second window
        
            self.button8 = Gtk.Button(label="Go Back")
            self.box2.append(self.button8)
            self.button8.set_margin_top(10)
            self.button8.set_margin_bottom(20)
            self.button8.set_margin_start(10)
            self.button8.set_margin_end(10)
            self.button8.connect('clicked', self.Go_Back)
            
#----------------------------------------------------------------------------------------------------


#Second Buton, on the main window. Opens a new window.
        
    def Install_Waydroid(self, button):
        # create a second application window to be called by a button from the primary application window.
 
        class InstallWaydroid(Gtk.ApplicationWindow):
        
            self.header = Gtk.HeaderBar()
            self.set_titlebar(self.header)
    
            self.set_default_size(360, 720)
            self.set_title("My Waydroid Manager")
            
            # Third Box, needed to put buttons inside of.
        
            self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box3)
            
            # Ninth button, second window, 'Build from source'
            
            self.button9 = Gtk.Button(label="Build from Source")
            self.box3.append(self.button9)
            self.button9.set_margin_top(200)
            self.button9.set_margin_bottom(20)
            self.button9.set_margin_start(10)
            self.button9.set_margin_end(10)
            self.button9.connect('clicked', self.Build_From_Source)
            
            # Tenth button 'Purge Waydroid Installation' , second window
        
            #self.button10 = Gtk.Button(label="Install W/ gdown from priv page")
            #self.box3.append(self.button10)
            #self.button10.set_margin_top(10)
            #self.button10.set_margin_bottom(20)
            #self.button10.set_margin_start(10)
            #self.button10.set_margin_end(10)
            #self.button10.connect('clicked', self.Install_With_Gdown)
        
            # Eleventh button 'Go Back' , second window
        
            self.button11 = Gtk.Button(label="Go Back")
            self.box3.append(self.button11)
            self.button11.set_margin_top(10)
            self.button11.set_margin_bottom(20)
            self.button11.set_margin_start(10)
            self.button11.set_margin_end(10)
            self.button11.connect('clicked', self.Go_Back)
            
#-----------------------------------------------------------------------------------------------------
           
    # This is where we will define what each button Does, and connect a function to each of them.
    
        
    #Button 3  
    def Advanced_Options(self, button):
        print("here's some more text, developer.")
      
    #Button 4    
    def Help(self, button):
        print("helpful text!")
    
    #Button 5
    def About(self, button):
        print("Informative texty stuffs")
        
    #Button 6
    def Install_Dependencies(self, button):
        # install dependencies for Waydroid
        print("Heyo Developer!!!!")
            
    #Button 7
    def Purge_Waydroid_Installation(self, button):
        # Purge Waydroid Installation
        print("wassssssuuuuuuuuup!!!!!")
          
    #Button 8
    def Go_Back(self, button):
        # Go back ot the previous Window
        print("going back!")
        self.win = MainWindow(application=app)
        self.win.present()
        
    #Button 9
    def Build_From_Source(self, button):
        # Install latest LineageOS from sourceforge
        print("one sec")
        #print(subprocess.run(["sudo chmod +x scripts/build.sh"], shell=False))
        #print(subprocess.run(["scripts",
                #"./build.sh"], shell=False))
        os.system("cd scripts && ./build.sh")
        
    
    #Button 10
    def Install_With_Gdown(self, button):
        print("some great placeholder text")
        
    
# This tells the app how to open Various Windows, And close them.
    
# This is where the 'Back' button needs to be defined:
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
        widget.hide()
        
# These lines tell the app what window to open when the app is launched
        
class MyWaydroidManager(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyWaydroidManager(application_id="com.KharraOswin.MyWaydroidManager")
app.run(sys.argv)
