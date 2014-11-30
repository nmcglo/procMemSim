from operator import itemgetter

class Schedule:

	mainsched = []

	def __init__(self, procs):
		unfoldedProcs = ''
		E = []

		N = len(procs)

		for i in range(0,N):
			name = procs[i].name
			mem = procs[i].mem

			for j in range(0,len(procs[i].sched)):
				(e,l) = procs[i].sched[j]
				E.append((e,name,'e',mem))
				E.append((l,name,'l',mem))

		E.sort()
		self.mainsched = E

	def getNextEvents(self, currentTime):
		i = 0
		while True:
			nextTime = self.mainsched[i][0]
			if nextTime >= currentTime:
				break
			i+=1

		A = []
		for event in self.mainsched:
			if event[0] == nextTime:
				A.append(event)

		return sorted(A, key=itemgetter(2), reverse=True)



