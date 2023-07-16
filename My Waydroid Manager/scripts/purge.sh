#!/bin/bash

if [ $(hostname) = 'mobian' ]; then
   echo "to be filled"
elif [ $(hostname) = 'ubuntu' ]; then
   echo "to be filled"
elif [ $(hostname) = 'manjaro' ]; then
   echo "to be filled"
elif [ $(hostname) = 'postmarketos*' ]; then
   echo "to be filled" 
else
   echo "Error 404"
fi
