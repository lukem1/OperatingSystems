#
# components.py
# OperatingSystems
#
# Luke McGuire
# Matt Walter
# 28 February 2020
#

# Process

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



# Scheduler

class RoundRobin:

    def __init__(self, sliceSize, memorySize):
        self.counter = 0  # Counter to cycle time slices
        self.time = 0  # Time since start of the simulated system
        self.current = -1  # Current process (index of proc list)
        self.sliceSize = sliceSize  # Size of time slice
        self.procs = []  # List of scheduled processes

    def schedule(self, job):

    def deschedule(self, jobindex):

    def update(self):
        self.counter += 1
        remaining = self.procs[self.current].run(self.time)
        if remaining == 0:
            self.deschedule(self.current)

        if self.counter == self.sliceSize:
            self.counter = 0
            self.current = (self.current + 1) % len(self.procs)