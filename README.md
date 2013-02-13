# smute.py

Smute.py is a Python script to mute Spotify ads.

It only works on Mac OS X.

The script listens for Spotify's NSDistributedNotifications and, whenever it detects
an advertisement, mutes the system audio by switching the audio source to a dummy 
output device.

### REQUIREMENTS

To run the script, you first need to install:

* **Soundflower**, a system extension for interapplication audio routing.  
    Download the latest version from <http://code.google.com/p/soundflower/downloads/list>

### USAGE

To mute Spotify ads, simply launch `SmutePy.app` and keep it running or. If you quit 
the main Spotify app, SmutePy also quits itself. 

If you like, you may also run the Python script `smute.py` from the Terminal. 

### CREDITS

SmutePy relies on [SwitchAudioSource](http://code.google.com/p/switchaudio-osx/), a 
command-line utility by [deweller](https://github.com/deweller) to switch the audio 
source on Mac OS X. 

I used [Platypus](http://www.sveinbjorn.org/platypus) to package the Python script 
inside a native OS X application (i.e., `SmutePy.app`).

### CONTACT

Cosimo Lupo  
lupocos [at] gmail [dot] com


