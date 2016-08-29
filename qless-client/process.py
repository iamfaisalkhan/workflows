import subprocess
import atexit
import os
import signal
import time
import threading
import uuid

global global_pid
global proc

from qless import logging

class Process(threading.Thread):
    def __init__(self, command, args=None, ID=None, workdir='.'):
        threading.Thread.__init__(self)

        self.pid = 0
        self.ID = ID

        if self.ID == None:
            self.ID = uuid.uuid1()
        
        self.parent_dir = script_dir
        # TODO: If commands doesn't exist, we can bailout here. 
        self.command = command
        self.args = args
        self._should_run = True
        self.workdir = workdir
        self.retcode = 1

    def run(self):
        if self.command == None:

        args = [self.command] + self.args

        f_stdout = "%s/%s.stdout"%(self.workdir, self.ID)
        f_stderr = "%s/%s.stderr"%(self.workdir, self.ID)

        fh_stdout = open(f_stdout, 'w')
        fh_stderr = open(f_stderr, 'w')

        p = subprocess.Popen(args, stdout=fh_stdout, stderr=fh_stderr, preexec_fn=os.setsid)

        global global_pid
        global_pid = p.pid

        while p.poll() is None and self._should_run:
            time.sleep(1)

        p.poll() is None and os.killpg(os.getpgid(p.pid), signal.SIGTERM)
        
        self.retcode = p.returncode

    def stop(self):
        self._should_run = False

# proc = Process('/local/fkhan/src/XPCS/xpcs-pipeline-dev/workflows/qless-client', 'shell.sh', ['5'])
# proc.start()
# print "New"

# proc.join()
