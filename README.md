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

### CREDITS

SmutePy relies on [SwitchAudioSource](http://code.google.com/p/switchaudio-osx/), a 
command-line utility by [deweller](https://github.com/deweller) to switch the audio 
source on Mac OS X. 

### STAND-ALONE APPLICATION

For ease of use, I also packaged the Python script inside a stand-alone native OS X application using [Platypus](http://www.sveinbjorn.org/platypus).

You can download the disk image "SmutePy-1.0.dmg" from this Dropbox link:

<https://www.dropbox.com/s/ngiaj4guueg763f/SmutePy-1.0.dmg>

### CONTACT

Cosimo Lupo  
lupocos [at] gmail [dot] com


