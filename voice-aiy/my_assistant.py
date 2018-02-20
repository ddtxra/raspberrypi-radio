#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys
import time

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
import RPi.GPIO as GPIO

from danikitlcd import lcd_message
from danikitbulb import light
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
#from yeelight import Bulb

#Defines the light bulb
#bulb = Bulb("192.168.178.164")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


RF_CODESEND="/home/pi/raspivoice-utils/RPi_utils/codesend "
RF_A_ON=RF_CODESEND + "1361"
RF_A_OFF=RF_CODESEND + "1364"

#def lcd_message(l1, l2):
#    subprocess.call('sudo python /home/pi/bin/lcd.py \"' + str(l1) + '\" \"' + str(l2) + '\"', shell=True)

def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)

playshell = None

# TODO
# Should play a song from youtube as described in here: https://drive.google.com/file/d/0B5s6SxCTcra3OE1ra3FFdk11aVk/view
# https://www.raspberrypi.org/forums/viewtopic.php?f=114&t=182665
def play(song):
    print(song)
    global playshell
    if (playshell == None):
        playshell = subprocess.Popen(["/usr/local/bin/mpsyt",""],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        playshell.stdin.write(bytes('/' + song + '\n1\n', 'utf-8'))
        playshell.stdin.flush()

    INPUT_PIN = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INPUT_PIN, GPIO.IN)

    while GPIO.input(INPUT_PIN) == True:
        time.sleep(0.1)

    aiy.audio.say("Music canceled ready for next one...")    
    pkill = subprocess.Popen(["/usr/bin/pkill","vlc"],stdin=subprocess.PIPE)

def sunny():
    #aiy.audio.say('Enjoy your day Daniel and Maria!')
    lcd_message("Good morning", "Daniel and Maria")
    subprocess.call(RF_A_ON, shell=True)

#https://www.hackster.io/vvanhee/internet-streaming-radio-with-google-aiy-1edff3
def radio_on():
    subprocess.call("sudo systemctl enable mpd", shell=True)
    #aiy.audio.say('Starting your lovely song for Maria Argento your princess and love and mother of your children')
    #subprocess.call("mpc clear;mpc add http://192.168.178.47:8000/perfect.mp3;mpc play", shell=True)
    subprocess.call("mpc clear;mpc add http://centova.radios.pt:9478;mpc play", shell=True)

def radio_off():
    subprocess.call("mpc stop;", shell=True)

def night():
    #aiy.audio.say('Enjoy your crazy night Daniel and Maria!')
    lcd_message("Enjoy your", "crazy night")
    subprocess.call(RF_A_OFF, shell=True)

def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)

def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        lcd_message("Listening...", "To you!")
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        lcd_message("you said", text)
        time.sleep(0.2)
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'radio on':
            assistant.stop_conversation()
            radio_on()
        elif 'light color' in text:
            color = text.replace('light color ', '', 1)
            assistant.stop_conversation()
            light(color)
        elif 'play song' in text:
            #Goes to YouTube, search for music and gets the first one
            song = text.replace('play song', '', 1)
            assistant.stop_conversation()
            play(song)
        elif text == 'radio off':
            assistant.stop_conversation()
            radio_off() 
        elif text == 'sunny':
            assistant.stop_conversation()
            sunny()
        elif text == 'night':
            assistant.stop_conversation()
            night()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
