import subprocess

class XPCSAnalysis(object):
    @staticmethod
    def gridftp(job):
    	subprocess.call(['/home/faisal/Development/workflows/qless-client/shell.sh'])
        job.complete('multitau')

    @staticmethod
    def multitau(job):
        job.complete('plot')

    @staticmethod
    def plot(job):
        job.complete()
