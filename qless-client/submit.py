
import qless

client = qless.Client()
queue = client.queues['multitau']


import xpcs
for i in range(1):
	queue.put(xpcs.XPCSAnalysis, {})
