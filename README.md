# smute.py

Smute.py is a Python script to mute Spotify ads which listens for Spotify's 
NSDistributedNotifications and, whenever it detects an advertisement, switches 
the audio source to a dummy output device. 

## REQUIREMENTS

* [Spotify](http://www.spotify.com/download) (needs to be installed in 
    the main /Applications folder)
* [Soundflower](http://code.google.com/p/soundflower/downloads/list), a system
    extension for interapplication audio routing.
