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

        global proc
        proc = Process(os.environ['EXE_DIR'], 'multitau.sh', ['-i', job['i']])
        proc.start()

        time_last_heartbeat = 0

	try:
           while proc.isAlive():
  	       print "Process id %d"%(os.getpid())
               time.sleep(10)
               job.heartbeat()

    	   if (proc.retcode != 0):
	       job.fail("Child process failed", "error")
    	   else:
	       job.complete()	
	except:
		cleanUp()
		exit(1)

    @staticmethod
    def gridftp(job):
        time.sleep(5)
        job.complete()

    @staticmethod
    def plot(job):
        time.sleep(6)
        job.complete()
