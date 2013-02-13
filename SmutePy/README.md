# smute.py

SmutePy is an application written in Python to mute Spotify ads.

It listens for Spotify's NSDistributedNotifications and, whenever it detects
an advertisement, mutes the system audio by switching the audio source to a dummy 
output device.

### REQUIREMENTS

To run SmutePy, you first need to install:

* **Soundflower**, a system extension for interapplication audio routing.  
    Download the latest version from <http://code.google.com/p/soundflower/downloads/list>

### INSTALLATION

To install SmutePy, simply copy it inside the '/Applications' folder.

### USAGE

To mute Spotify ads, simply launch `SmutePy.app` and keep it running while you play songs 
on Spotify.

### CREDITS

SmutePy relies on [SwitchAudioSource](http://code.google.com/p/switchaudio-osx/), a 
command-line utility by [deweller](https://github.com/deweller) to switch the audio 
source on Mac OS X. 

I used [Platypus](http://www.sveinbjorn.org/platypus) to package the Python script 
(i.e., `smute.py`) inside a native OS X application (i.e., `SmutePy.app`).

### CONTACT

Cosimo Lupo  
lupocos [at] gmail [dot] com


