"""
Sahaana
Things needed:
audiolab
pydub
yasm
ffmpeg
"""

import scikits.audiolab as audiolab
from pydub import AudioSegment
from time import sleep
from pylab import *

import os

fs = 44100

def store_as_wav(audioTrack):
    if audioTrack.endswith('.wav'):
        song = AudioSegment.from_file(audioTrack, "wav")
    elif audioTrack.endswith('.m4a'):
        song = AudioSegment.from_file(audioTrack, "m4a")
    else:
        song = AudioSegment.from_file(audioTrack, "mp3")
    wave_song = song.export('temp.wav', format='wav')

def stream_power(chunksize=512, num_powers=8):
    """
    break mp3file into chunks of size chunksize
    compute the num power of norms (coefficients to output)
    print out output at rate of fs/chunksize and play song
    """
    
    (snd, sampFreq, nBits) = audiolab.wavread('temp.wav')
    signal = snd[:,0]
    coeffs = []
    for i in range(0, len(signal), chunksize):
        for j in range(i, i+chunksize, chunksize/num_powers):
            coeffs.append(norm(signal[j:j+chunksize/num_powers]))

    for coeff in coeffs:    
        #TODO: figure out how long to sleep for
        time_sleeping = fs/chunksize
        sleep(time_sleeping)
        print coeff
    return coeffs
    
def teardown():
    os.remove('temp.wav')

store_as_wav("gatw.mp3")
a = stream_power()
teardown()
