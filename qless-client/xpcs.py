import subprocess
import time
import atexit

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
        proc = Process('/local/fkhan/src/XPCS/xpcs-pipeline-dev/workflows/qless-client', 'shell.sh', ['15'])
        proc.start()

        print("Testing heartbeat")

        time_last_heartbeat = 0

        while proc.isAlive():
            time.sleep(2)
            job.heartbeat()

        job.complete()