# components.py
# OperatingSystems
#
# Luke McGuire
# Matt Walter
# 28 February 2020
#


class PageTable:

    def __init__(self, pageSize, memSize):
        self.size = memSize // pageSize
        self.pageSize = pageSize
        self.memSize = memSize
        self.available = memSize
        self.table = []

        for i in range(0, self.size):
            self.table.append('.')

        print(self.table)


class Process:

    def __init__(self, pid, size, runtime):
        self.pid = pid
        self.size = size
        self.time = runtime
        self.start = -1
        self.end = -1

    def run(self, systime):
        if self.start == -1:
            self.start = systime

        self.time -= 1

        if self.time == 0:
            self.end = systime + 1

        return self.time
        
    def selfPrint(self):
        print("Pid: ", self.pid)
        print("Size: ", self.size)
        print("runTime: ", self.time)


class RoundRobin:

    def __init__(self, sliceSize, memorySize, pagetable):
        self.table = pagetable  # Page table
        self.queue = []  # Jobs waiting to be scheduled
        self.jobs = []  # Currently scheduled jobs
        self.counter = 0  # Counter to cycle time slices
        self.time = 0  # Time since start of the simulated system
        self.current = -1  # Current process (index of jobs list)
        self.sliceSize = sliceSize  # Size of time slice

    # TODO: Don't overallocate pages
    #ef schedule(self, job):

    #def deschedule(self, jobindex):

    """ def update(self):
        self.counter += 1
        remaining = self.procs[self.current].run(self.time)
        if remaining == 0:
            self.deschedule(self.current)

        if self.counter == self.sliceSize:
            self.counter = 0
            self.current = (self.current + 1) % len(self.procs) """