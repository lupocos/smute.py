# smute.py

Smute.py is a Python script to mute Spotify ads. 

The script listens for Spotify's NSDistributedNotifications and, whenever it detects
an advertisement, mutes the system audio by switching the audio source to a dummy 
output device.

It includes [SwitchAudioSource](http://code.google.com/p/switchaudio-osx/), a 
command-line utility by [deweller](https://github.com/deweller) to switch the audio 
source on Mac OS X. 

The script requires [Soundflower](http://code.google.com/p/soundflower/downloads/list), 
a system extension for interapplication audio routing -- besides of course the 
official [Spotify](http://www.spotify.com/download) app (which must be installed in 
the main `/Applications` folder for the script to work).

I packaged the script inside a native OS X application (`SmutePy.app`), 
using [Platypus](http://www.sveinbjorn.org/platypus).

To mute Spotify ads, simply launch the app and keep it running.
