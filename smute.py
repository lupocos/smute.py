#!/usr/bin/python
'''
Smute.py is a python script to mute Spotify ads. It listens for Spotify 
NSDistributedNotifications and switches the audio source to a 
dummy output device whenever it detects an advertisement.   
'''
import Foundation
import os
import time
import subprocess
import sys
from AppKit import *
from PyObjCTools import AppHelper

def is_installed():
    installed = subprocess.check_output(
        'SwitchAudioSource -a', 
        shell=True,
        stderr=subprocess.STDOUT,
        )
    if 'Soundflower (2ch) (output)' in installed and os.path.exists('/Applications/Spotify.app'):
        return True
    return False

def is_running(process):
    tmp = os.popen("ps -Af").read()
    if process not in tmp[:]:
        return False
    else:
        return True
            
def is_ad(desc): # returns True when the track is an advertisement
    return "http://" in desc or "https://" in desc or "www." in desc or "spotify:album:" in desc or "spotify:app:" in desc or "spotify:user:" in desc or "spotify:track:" in desc

if is_installed():   
    pathname = os.path.dirname(sys.argv[0])        
    abspathname = os.path.abspath(pathname)
    
    if not is_running('Spotify.app'):
        os.system('open /Applications/Spotify.app')
        time.sleep(3)

    currentdevice = subprocess.check_output(abspathname+
        '/SwitchAudioSource -c', 
        shell=True,
        stderr=subprocess.STDOUT,
        ).split('\n')
    currentdevice = currentdevice[0]
    print 'Current audio device =', currentdevice

    set_mute = abspathname+'/SwitchAudioSource -s "Soundflower (2ch)"'
    unset_mute = abspathname+'/SwitchAudioSource -s "'+currentdevice+'"'

    mute = False
    ad = False
    class GetSongs(NSObject):
        def getMySongs_(self, song):
            global mute
            global ad
            song_details = {}
            ui = song.userInfo()
            if 'Playing' in ui['Player State']:
                ad = is_ad(ui['Album'])
                if ad and not mute:
                    mute = True
                    print ''
                    print 'Ad detected:'
                    os.system(set_mute)
                elif not ad and mute:
                    mute = False
                    print ''
                    print 'Not an ad:'
                    os.system(unset_mute)
            elif 'Stopped' in ui['Player State']:
                time.sleep(2)
                if not is_running('Spotify.app'):
                    sys.exit()
         
    nc = Foundation.NSDistributedNotificationCenter.defaultCenter()
    GetSongs = GetSongs.new()
    nc.addObserver_selector_name_object_(GetSongs, 'getMySongs:', 'com.spotify.client.PlaybackStateChanged',None)
    AppHelper.runConsoleEventLoop()





