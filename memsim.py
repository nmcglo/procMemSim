#Memsim.py - Operating Systems Homework 4
#Group Project --  'Mark Plagge', Neil McGlohon
#Main runner for the memorySim:

import sys

from Process import *
from Schedule import *
from Memory import *


def parseProcess(procString):
    procList = procString.split()
    procName = procList[0]
    procMem = int(procList[1])
    rawSchedule = procList[2:len(procList)]
    schedule = parsePairs(rawSchedule)

    proc = Process(procName, procMem, schedule)

    return proc


def parsePairs(pairList):
    pairNum = len(pairList) / 2

    tupleList = []
    for i in range(0, pairNum):
        one = int(pairList[(i + 1) * 2 - 2])
        two = int(pairList[(i + 1) * 2 - 1])
        tupleList.append((one, two))
    return tupleList



def usage():
    print("USAGE: memsim [-q] <input-file> { first | best | next | worst}")
# Main*********************************
valid_opts = set(["noncontig", "first", "best", "next", "worst"])
inOpts = set(sys.argv)
if len(sys.argv) < 2:
    #UNACCEPTABLE!
    usage()
elif len(valid_opts.union(inOpts)) == 0:
    usage()
    print("Needs a memory simulation type")
    print(sys.argv)

else:
    qFlag = False
    if '-q' in sys.argv:
        qi = sys.argv.index('-q')
        sys.argv.pop(qi)
        qFlag = True

    filename = sys.argv[1]
    option = sys.argv[2]

    alg = 0
    if option == 'first':
        alg = 1
    elif option == 'best':
        alg = 2
    elif option == 'next':
        alg = 3
    elif option == 'worst':
        alg = 4
    elif option == 'noncontig':
        alg = 5

    inputFile = open(filename, 'r')
    text = inputFile.read()

    # Create list of processes
    Procs = text.split('\n')
    N = int(Procs[0])
    Procs = Procs[1:len(Procs)]

    P = []
    for i in range(0, N):
        P.append(parseProcess(Procs[i]))

    # Get last time
    lastTime = []
    for i in range(0, N):
        lastTime.append(max(P[i].sched[-1]))
    ENDTIME = max(lastTime)

    mainSched = Schedule(P)
    mem = Memory(alg)


    # MAIN SIMULATION LOOP ********************
    print('-' * 80)
    print('Starting Simulation...\n')
    print('Simulation Parameters:')
    print('Algorithm'.ljust(20) + 'Number of Procs'.ljust(20) + 'Quiet Mode'.ljust(20))
    print(option.capitalize().ljust(20) + str(N).ljust(20) + str(qFlag).ljust(20))

    currentTime = 0
    promptTime = 0
    procCount = 0
    while True:
        if not qFlag:

            while True:
                promptTime = raw_input("Enter a time for the simulation to pause: ")
                if len(promptTime) == 0:
                    print("Please enter a command.")
                else:
                    promptTime = int(promptTime)
                    if promptTime == 0:
                        print("Exiting")
                        exit()
                    if promptTime < currentTime:
                        print("Cannot enter a time that has already passed. Try again.")
                    else:
                        break

        nextEvents = mainSched.getNextEvents(currentTime)
        while (currentTime <= promptTime) | (currentTime <= nextEvents[0][0]):
            nextEvents = mainSched.getNextEvents(currentTime)
            if (currentTime == nextEvents[0][0]):

                for event in nextEvents:
                    if event[2] == 'e':
                        er = mem.addProc(event)
                        if er == -1:
                            mem.defrag(currentTime, procCount)
                            er2 = mem.addProc(event)
                            if er2 == -1:
                                print("Out-Of-Memory Error: Exiting Simulation")
                                print("Tried to add process: " + event[1])
                                print("Memory Dump: Time: %i" % (currentTime))
                                print(mem)
                                sys.exit(1)
                        procCount += 1
                    if event[2] == 'l':
                        mem.removeProc(event)
                        procCount -= 1

            if (currentTime == nextEvents[0][0]) | (currentTime == promptTime):
                print('Memory at time: ' + str(currentTime))
                print(mem)
                print('\n')

            currentTime += 1
            if currentTime > promptTime or currentTime == ENDTIME + 1:
                break

        if currentTime == ENDTIME + 1:
            print("Reached the end of the simulation.")
            break









