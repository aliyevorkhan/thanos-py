import sys
from glob import glob
import os
import random
import sounddevice as sd
import numpy as np

def snap(dir):
    files = glob(dir+'/*')
    random.shuffle(files)
    for count, file in enumerate(files):
        if count%2==0:
            os.remove(file)

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm)>200:
        print ("You have been deleted half of the all files!")
        snap(str(sys.argv[1]))

if __name__=='__main__':
    
    with sd.Stream(callback=print_sound):
        sd.sleep(int(sys.argv[2]))
