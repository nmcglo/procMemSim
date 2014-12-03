import textwrap
import sys


class Memory:
    firstFit = 1
    bestFit = 2
    nextFit = 3
    worstFit = 4
    noncontig = 5
    lastPos = 0


    def __init__(self, alg):
        self.alg = alg
        self.freeMem = 1600
        self.mainMem = '.' * 1600
        memList = list(self.mainMem)
        for i in range(0, 80):
            memList[i] = '#'
            self.freeMem -= 1
        self.mainMem = memList


    def addProc(self, procEvent):
        procName = procEvent[1]
        memReq = procEvent[3]

        if (self.alg == self.firstFit):
            loc = self.findFitLocation(memReq, self.firstFit)
            if loc != -1:
                for i in range(loc, loc + memReq):
                    self.mainMem[i] = procName
                return 1
            else:
                return -1

        if (self.alg == self.bestFit):
            loc = self.findFitLocation(memReq, self.bestFit)
            if loc != -1:
                for i in range(loc, loc + memReq):
                    self.mainMem[i] = procName
                return 1
            else:
                return -1

        if (self.alg == self.nextFit):
            loc = self.findFitLocation(memReq, self.nextFit, lastPos=self.lastPos)
            if loc != -1:
                for i in range(loc, loc + memReq):
                    self.mainMem[i] = procName
                self.lastPos = loc + memReq
                return 1
            else:
                return -1

        if (self.alg == self.worstFit):
            loc = self.findFitLocation(memReq, self.worstFit)
            if loc != -1:
                for i in range(loc, loc + memReq):
                    self.mainMem[i] = procName
                return 1
            else:
                return -1

        if (self.alg == self.noncontig):
            if self.freeMem >= memReq:
                self.freeMem -= memReq
                r = 0
                i = 0
                while r < memReq:
                    if self.mainMem[i] == '.':
                        self.mainMem[i] = procName
                        r += 1
                    i += 1
                return 1

            else:
                print("Out-Of-Memory Error: Exiting Simulation")
                sys.exit(1)
                return -1

    def removeProc(self, procEvent):
        procName = procEvent[1]
        memstr = ''.join(self.mainMem)
        procMem = memstr.count(procName)
        if procMem == 0:
            return
        memstr = memstr.replace(procName, '.')
        self.mainMem = list(memstr)
        self.freeMem += procMem


    def findFitLocation(self, memReq, option, lastPos=0):
        freeLocations = self.getFreeMemLocations()

        if option == self.firstFit:
            memstr = ''.join(self.mainMem)
            try:
                startLoc = memstr.index('.' * memReq)
            except:
                startLoc = -1
            return startLoc

        if option == self.bestFit:

            mindiff = sys.maxint
            minloc = -1
            for loc in freeLocations:
                diff = abs(loc[1] - memReq)
                if (diff < mindiff) & (loc[1] >= memReq):
                    mindiff = diff
                    minloc = loc[0]

            return minloc

        if option == self.nextFit:
            memstr = ''.join(self.mainMem)
            try:
                startLoc = memstr.index('.' * memReq, lastPos)
            except:
                try:
                    startLoc = memstr.index('.' * memReq)
                except:
                    startLoc = -1
            return startLoc

        if option == self.worstFit:
            maxdiff = -1
            maxloc = -1
            for loc in freeLocations:
                diff = abs(loc[1] - memReq)
                if (diff > maxdiff) & (loc[1] >= memReq):
                    maxdiff = diff
                    maxloc = loc[0]

            return maxloc

    def getFreeMemLocations(self):
        A = []
        i = 0
        while True:
            try:
                i = ''.join(self.mainMem).index('.', i)
                index = i
            except:
                break
            blockSize = 0
            while self.mainMem[i] == '.':
                blockSize += 1
                i += 1
                if i == len(self.mainMem):
                    break
            A.append((index, blockSize))
        return A


    def defrag(self, time, N):
        print("Performing defragmentation...")

        print("Memory before defragmentation:")
        print(self)
        print('')

        mem = ''.join(self.mainMem)
        i = mem.count('.');
        mem = mem.replace('.', '');
        mem = mem + '.' * i;
        self.mainMem = list(mem)

        print("Defragmentation complete.")
        print('Relocated %i processes to create a free memory block of %i units \n(%.2f%% of total memory).\n' % (N, i,( i / 1600. * 100)))
        print('Memory after defragmentation at time: %i' % (time))
        print(self)


    def __str__(self):
        outList = textwrap.wrap(''.join(self.mainMem), width=80)

        outList2 = []
        for line in outList:
            tempLine = line + '\n'
            outList2.append(tempLine)

        return ''.join(outList2)






