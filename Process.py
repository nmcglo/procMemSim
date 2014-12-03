class Process:
    def __init__(self, name, mem, sched):
        self.name = name
        self.mem = mem
        self.sched = sched

    def __str__(self):
        mystr = 'Name: %s\nMemory Required: %i\nSchedule: %s' % (self.name, self.mem, self.sched)
        return mystr

    def __lt__(self, other):
        
        return (self.sched[self.sched.count() - 1][1] < other.sched[other.sched.count() - 1][1]);