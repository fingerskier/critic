import random

class Queue:
	def __init__(self, max_wip, max_flow):
		self.queued = 0
		self.wip = 0

		# work-in-progress (" ready pool")
		self.max_wip = max_wip
		self.max_flow = max_flow # avg outflow is max_flow/ 2

	def work(self, u):

		# Add to ready pool
		u = max(0, int(round(u)))
		u = min(u, self.max_wip)

		self.wip += u

		# Transfer from ready pool to queue
		r = int(round(random.uniform(0, self.wip)))
		self.wip -= r
		self.queued += r

		# Release from queue to downstream process
		r = int(round(random.uniform(0, self.max_flow)))
		r = min(r, self.queued)
		self.queued -= r 

		return self.queued
