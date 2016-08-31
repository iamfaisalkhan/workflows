import subprocess
import time
import atexit
import os

from process import Process

from qless import logger

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
        
        logger.info("Launching multitau.sh process in dir %s"%(os.environ['EXE_DIR']))
        command = "%s/%s"%(os.environ['EXE_DIR'], 'multitau.sh')
        
        args = []
        if 'input' in job:
            args.append('-i')
            args.append(job['input'])
        else:
            job.fail("Input argument", "Input file path is missing from job definition")

        if 'endpoint' in job:
            args.append('-e')
            args.append(job['endpoint'])

        proc = Process(command, args)
        proc.start()

        time_last_heartbeat = 0
        try:
            while proc.isAlive():
                time.sleep(10)
                job.heartbeat()

            if (proc.retcode != 0):
                #TODO better error reporting
                job.fail("Child process failed", "error")
            else:
                job.complete()   
        except:
            cleanUp()
            exit(1)

    @staticmethod
    def gridftp(job):
        global proc

        args = []

        # if 'source' in job:
        #     args.append(job['source'])
        # else:
        #     job.fail("Input arguments", "The source files parameter missing from job definition")

        # if 'dest' in job:
        #     args.append(job['dest'])
        # else:
        #     job.fail("Input arguments", "The destinition file parameter missing from job definition")

        # if 'args' in job:
        #     args = job['args'].split( ) + args

        # print args
        # logger.info("Launching globus_url_copy with source=%s and dest=%s " %(source, dest))

        # job.complete()

        args.append(job['source'])
        args.append(job['dest'])

        command = "%s/%s"%(os.environ['QLESS_DIR'], 'gridftp.sh')

        proc = Process(command, args)
        proc.start()

        try:
            while proc.isAlive():
                job.heartbeat()
                time.sleep(25)

            if proc.retcode != 0:
                job.fail("exit(1)", "error")
            else:
                job.complete()
        except:
            cleanUp()
            exit(1)
        