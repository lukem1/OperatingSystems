# components.py
# OperatingSystems
#
# Luke McGuire
# Matt Walter
# 28 February 2020
#

import math

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

    def allocate(self, pages, job):
        self.available -= job.size
        for i in range(0, len(self.table)):
            if self.table[i] == '.':
                self.table[i] = job.pid
                pages -= 1
            if pages == 0:
                return

    def deallocate(self, job):
        for i in range(0, len(self.table)):
            if self.table[i] == job.pid:
                self.table[i] = '.'

        self.available += job.size

    def toString(self):
        return self.table


class Process:

    def __init__(self, pid, size, runtime):
        self.pid = pid
        self.size = size
        self.time = runtime
        self.arrival = -1
        self.start = -1
        self.end = -1

    def run(self, simtime):
        if self.start == -1:
            self.start = simtime

        self.time -= 1

        if self.time == 0:
            self.end = simtime + 1

        return self.time
        
    def selfPrint(self):
        print("Pid: ", self.pid)
        print("Size: ", self.size)
        print("runTime: ", self.time)


class RoundRobin:

    def __init__(self, sliceSize, pagetable):
        self.table = pagetable  # Page table
        self.queue = []  # Jobs waiting to be scheduled
        self.jobs = []  # Currently scheduled jobs
        self.counter = 0  # Counter to cycle time slices
        self.time = 0  # Time since start of the simulated system
        self.current = 0  # Current process (index of jobs list)
        self.sliceSize = sliceSize  # Size of time slice

    # TODO: Don't overallocate pages
    def schedule(self, job):
        if self.table.available >= job.size: # TODO Fix
            self.jobs.append(job)
            requiredPages = int(math.ceil(job.size / self.table.pageSize))
            self.table.allocate(requiredPages, job)
        else:
            self.queue.append(job)

    def deschedule(self, job):
        self.jobs.remove(job)
        self.table.deallocate(job)

        if len(self.queue) != 0:
            q = self.queue
            self.queue = []

            for j in q:
                self.schedule(j)

    def update(self):
        self.counter += 1
        remaining = self.jobs[self.current].run(self.time)
        if remaining == 0:
            self.deschedule(self.jobs[self.current])

        if len(self.jobs) != 0:
            return True

        if self.counter == self.sliceSize:
            self.counter = 0
            self.current = (self.current + 1) % len(self.jobs)

        
        return False

    def procsPrint(self):
        if len(self.jobs) != 0:
            print("Current job: ", self.jobs[self.current].pid)
        print("---queue---")
        for j in self.queue:
            j.selfPrint()
        print("---jobs---")
        for j in self.jobs:
            j.selfPrint()

        print(self.table.toString())