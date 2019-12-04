import threading
import time

#practise thread functions

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, name, data):
		threading.Thread.__init__(self)
		self.setName(name)
		self.data = data

	def run(self):
		print('Start executing: ' + self.getName())
		#print('Running current thread: ' + str(threading.currentThread()))
		counter()
		print('Exiting: ' + self.getName())

def counter():
	i=100
	while i:
		time.sleep(0.1)
		i -= 1

threads = []

for i in range(10):
	name = 'Thread-' + str(i)
	threads.append(myThread(name,i))

for i in range(len(threads)):
	threads[i].start()

print()
print('***')
print()

#threading.activeCount() − Returns the number of thread objects that are active.
print('Number of active threads: ' + str(threading.activeCount()))
#threading.currentThread() − Returns the number of thread objects in the caller's thread control.
print('Number of thread objects in the caller\'s thread control: ' + str(threading.currentThread()))
#threading.enumerate() − Returns a list of all thread objects that are currently active.
print('List of all thread objects that are currently active: ' + '\n' + str([i for i in threading.enumerate()]))

print()
print('***')
print()
