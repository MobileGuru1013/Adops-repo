from gtts import gTTS
import pyglet
import time
import os


def tts(text):
    _file = gTTS(text=text, lang='en')
    filename = 'voice.mp4'
    _file.save(filename)

    music = pyglet.media.load(filename)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)