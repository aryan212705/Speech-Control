import os
from pocketsphinx import LiveSpeech
import scripts
import threading
import pyaudio
from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from commands import *
from priority import *


def all_present(keywords, pattern):
    for word in pattern:
        if word not in keywords:
            return False
    return True


def check_priority(cmds):
    global priority
    abc = cmds[:]
    for cmd in abc:
        if priority.__contains__(cmd):
            for i in abc:
                if i in priority[cmd] and i in cmds:
                    cmds.remove(i)
    if len(cmds) == 1:
        return cmds[-1]
    return 0


def detect_cmd(phrase):
    global commands
    phrase = phrase.lower()
    keywords = phrase.split()
    cmds = []
    for cmd in commands.keys():
        for pattern in commands[cmd]:
            if all_present(keywords, pattern):
                cmds.append(cmd)
                break
    res = check_priority(cmds)
    if res:
        return res
    return 0
    
        
def recognition():
    MODELDIR = os.getcwd() + '/'
    
    config = Decoder.default_config()
    config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
    config.set_string('-lm', path.join(MODELDIR, 'en-us.lm'))
    config.set_string('-dict', path.join(MODELDIR, 'en-us.dic'))
    decoder = Decoder(config)
    
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream() 
    
    in_speech_bf = False
    decoder.start_utt()
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
            if decoder.get_in_speech() != in_speech_bf:
                in_speech_bf = decoder.get_in_speech()
                if not in_speech_bf:
                    decoder.end_utt()
                    phrase = decoder.hyp().hypstr
                    print ('Result:', phrase)
                    cmd = detect_cmd(str(phrase))
                    if cmd == "dictation_mode":
                        stream.stop_stream()
                        getattr(scripts, cmd)()
                        stream.start_stream()
                    elif cmd:
                        getattr(scripts, cmd)()
                    decoder.start_utt()
        else:
            break
    decoder.end_utt()
    
if __name__ == "__main__":
    recognition()
