import threading
import time
import queue

#multithreading + priority queue

exitflag = 1

class myThread(threading.Thread):

	def __init__(self, name, queue):
		threading.Thread.__init__(self)
		self.name = name
		self.queue = queue

	def run(self):
		print('Starting: ' + self.name)
		process_data(self.name, self.queue)
		print('Exiting: ' + self.name)

def process_data(name, queue):
	while exitflag:
		queueLock.acquire()
		if not workQueue.empty():
			data = queue.get()
			queueLock.release()
			print(name + ' has processed data: ' + data)
			time.sleep(5)
		else:
			queueLock.release()
		time.sleep(1)

threadID = 1
threads = []
threadNames = ['Thread-01', 'Thread-02', 'Thread-03']
data = ['car', 'table', 'chair', 'computer', 'rocket', 'phone']
workQueue = queue.Queue(10)

queueLock = threading.Lock()

for i, ths in enumerate(threadNames):
	threads.append(myThread(ths,workQueue))
	threads[i].start()


queueLock.acquire()
for i in data:
	workQueue.put(i)

queueLock.release()

while not workQueue.empty():
	pass

exitflag = 0

for ths in threads:
	ths.join()

print('Exiting: ' + str(threading.currentThread()))

