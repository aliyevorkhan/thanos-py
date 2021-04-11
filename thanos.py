import sys
from glob import glob
import os
import random

def snap(dir):
    files = glob(dir+'/*')
    random.shuffle(files)
    for count, file in enumerate(files):
        if count%2==0:
            os.remove(file)

if __name__=='__main__':
    snap(str(sys.argv[1]))