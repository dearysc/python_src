import random,time,Queue
from multiprocessing.managers import BaseManager
#queue for sending
task_queue = Queue.Queue()
#queue for receiving
result_queue = Queue.Queue()

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue',callable = lambda:task_queue)
QueueManager.register('get_result_queue',callable = lambda:result_queue)

manager = QueueManager(address=('',8888),authkey = 'ysc')
#start Queue
manager.start()
#get the Queue object
task = manager.get_task_queue()
result = manager.get_result_queue()

#put some tasks 
for i in range(10):
	n = random.randint(0,10000)
	print 'Put task %d...' % n
	task.put(n)

#get the result
print 'Try get results...'
for i in range(10):
	r = result.get(timeout = 10)
	print 'Result:%s' % r

#shutdown 
manager.shutdown()


