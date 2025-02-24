
                  ___           ___           ___           ___
    ___          /  /\         /  /\         /__/\         /  /\          ___
   /  /\        /  /::\       /  /:/_        \  \:\       /  /::\        /  /\
  /  /:/       /  /:/\:\     /  /:/ /\        \__\:\     /  /:/\:\      /  /:/
 /__/::\      /  /:/  \:\   /  /:/ /::\   ___ /  /::\   /  /:/  \:\    /  /:/
 \__\/\:\__  /__/:/ \__\:\ /__/:/ /:/\:\ /__/\  /:/\:\ /__/:/ \__\:\  /  /::\
    \  \:\/\ \  \:\ /  /:/ \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\
     \__\::/  \  \:\  /:/   \  \::/ /:/   \  \::/       \  \:\  /:/  \__\/  \:\
     /__/:/    \  \:\/:/     \__\/ /:/     \  \:\        \  \:\/:/        \  \:\
     \__\/      \  \::/        /__/:/       \  \:\        \  \::/          \__\/
                 \__\/         \__\/         \__\/         \__\/  ioshot by Daryll Deatherage

usage: ioshot.py [-h] -f FILE -d DIRECTORY [-t THREADS] [-https] [-http] [-no-http]
python ioshot.py -f  file.txt -d /Desktop/sitepics -t 10 -no-http
Capture website screenshots using Selenium.

options:
  -h, --help            show this help message and exit
  -f, --file FILE       File containing URLs
  -d, --directory DIRECTORY
                        Directory to save screenshots
  -t, --threads THREADS
                        Number of threads to run concurrently
  -https                Capture only HTTPS sites (only if you file contains https only)
  -http                 Capture only HTTP sites (only if your file contains http only)
  -no-http             ( if your file.txt does not contain the Http:// or Https://) Treat URLs without 'http://' or 'https://' as HTTPS

requirements

selenium
pillow


































