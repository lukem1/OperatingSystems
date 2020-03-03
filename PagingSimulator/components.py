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
        self.available = self.size
        self.table = []

        for i in range(0, self.size):
            self.table.append('.')

    def allocate(self, pages, job):
        self.available -= pages
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
                self.available += 1

    def printer(self):
        for i in range(1, self.size+1):
            print(self.table[i-1], end='')
            if i % 4 == 0:
                print(' ', end='')
            if i % 16 == 0:
                print()


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
        
    def printer(self):
        print("pid: %d, size: %d, remaining time: %d" % (self.pid, self.size, self.time))


class RoundRobin:

    def __init__(self, sliceSize, pagetable):
        self.table = pagetable  # Page table
        self.queue = []  # Jobs waiting to be scheduled
        self.jobs = []  # Currently scheduled jobs
        self.counter = 0  # Counter to cycle time slices
        self.time = 0  # Time since start of the simulated system
        self.current = 0  # Current process (index of jobs list)
        self.sliceSize = sliceSize  # Size of time slice

    def schedule(self, job):
        requiredPages = int(math.ceil(job.size / self.table.pageSize))
        if self.table.available >= requiredPages:
            self.jobs.append(job)

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

        self.time += 1
        if len(self.jobs) == 0:
            return False

        if self.counter == self.sliceSize:
            self.counter = 0
            self.current = (self.current + 1) % len(self.jobs)

        return True

    def printer(self):
        print("-----Time %d-----" % self.time)
        if len(self.jobs) != 0:
            print("Current job: ", self.jobs[self.current].pid)
        print("---queue---")
        for j in self.queue:
            j.printer()
        print("---jobs---")
        for j in self.jobs:
            j.printer()
        print("---page table---")
        self.table.printer()
