import qless
import xpcs

client = qless.Client()
job1_id = client.queues['multitau'].put(xpcs.XPCSAnalysis, {'i':})

#job2_id = client.queues['gridftp'].put(xpcs.XPCSAnalysis, {'arg': 2}, depends=[job1_id])
#job3_id = client.queues['plot'].put(xpcs.XPCSAnalysis, {'arg': 3}, depends=[job1_id, job2_id])


# for i in range(1):
# 	queue.put(xpcs.XPCSAnalysis, {})
