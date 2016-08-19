import subprocess
import time
import atexit
import os

from process import Process

global proc

def cleanUp():    
    proc.stop()
    proc.join()

class XPCSAnalysis(object):
    def __init__(self):
        print "Initializing"

    @staticmethod
    def multitau(job):
        atexit.register(cleanUp)

        global proc
        proc = Process(os.environ['EXE_DIR'], 'shell.sh', ['15'])
        proc.start()

        print("Testing heartbeat")

        time_last_heartbeat = 0

        while proc.isAlive():
            time.sleep(2)
            job.heartbeat()

        job.complete()

    @staticmethod
    def gridftp(job):
        time.sleep(5)
        job.complete()

    @staticmethod
    def plot(job):
        time.sleep(6)
        job.complete()