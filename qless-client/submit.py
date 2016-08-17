import qless

client = qless.Client()
queue = client.queues['gridftp']


import xpcs
for i in range(2):
	queue.put(xpcs.XPCSAnalysis, {})