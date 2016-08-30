import qless
import xpcs

client = qless.Client('redis://hpcs08:63791')
#job1_id = client.queues['multitau'].put(xpcs.XPCSAnalysis, {'i': '/home/xpcs/D001_Aerogel_Clamped_Sq0_001_0001-0138.hdf'})
#job2_id = client.queues['multitau'].put(xpcs.XPCSAnalysis, {'i': '/home/xpcs/A001_D56_FF_att0_Fq0_001_0001-10000.hdf'})
#job2_id = client.queues['gridftp'].put(xpcs.XPCSAnalysis, {'src': 2, 'dest': 'dest'}, depends=[job1_id])
#job3_id = client.queues['plot'].put(xpcs.XPCSAnalysis, {'arg': 3}, depends=[job1_id, job2_id])
job1 = client.queues['gridftp'].put(xpcs.XPCSAnalysis, {'source': 'ftp://wolf08:2811/data/xpcs8/2015-3/leheny201511/D018_CPCl200NaSal118_Aurods_13C_att0_FCCDq1_001/',
                                                    'dest': 'ftp://hpc08:2812/user/fkhan/fdta1/'})



# for i in range(1):
# 	queue.put(xpcs.XPCSAnalysis, {})
