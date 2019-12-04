import threading
import time

class myThread(threading.Thread):

	def __init__(self, threadID, name, counter, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.delay = delay

	def run(self):
		print('Starting: ' + self.name)
		threadLock.acquire()
		print_time(self.name, self.counter, self.delay)
		threadLock.release()
		print('Exiting: ' + self.name)

def print_time(name, counter, delay):
	while counter:
		time.sleep(delay)
		print(name + ' time: ' + time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()

threads = []

threads.append(myThread(1,'Thread-1',100,0.01))
threads.append(myThread(2,'Thread-2',100,0.01))
threads.append(myThread(3,'Thread-3',100,0.01))

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Exiting main thread!')
