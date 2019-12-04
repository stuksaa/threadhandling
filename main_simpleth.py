import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadID, name, delay, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.delay = delay
		self.counter = counter

	def run(self):
		print('Starting thread: ' + self.name)

		print_time(self.name, self.counter, self.delay)		
		
		print('Exiting thread: ' + self.name)


def print_time(threadName, counter, delay):
	while counter:
		time.sleep(delay)
		print(threadName + ' time: ' + str(time.ctime(time.time())))
		counter -= 1


threads = []

threads.append(myThread(1, 'Thread-1', 0.05, 100))
threads.append(myThread(2, 'Thread-2', 0.03, 100))
threads.append(myThread(3, 'Thread-3', 0.01, 100))

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Exiting main thread!')
