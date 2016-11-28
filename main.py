from Queue import Queue
from Controller import Controller

def open_loop(p, tm = 5000):
	def target(t):
		return 5.0 # 5.1

	for t in range(tm):
		u = target(t)
		y = p.work(u)
		print t, u, 0, u, y

def closed_loop(c, p, tm = 5000):
	def setpoint(t):
		if t < 100: return 0
		if t < 300: return 50
		return 10

	y = 0
	for t in range(tm):
		r = setpoint(t)
		e = r - y
		u = c.work(e)
		y = p.work(u)
		print t, r, e, u, y


c = Controller(1.25, 0.01)
p = Queue(100, 25)

open_loop(p, 1000)

# closed_loop(c, p, 1000)