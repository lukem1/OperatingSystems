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

# Scheduler

class RoundRobin:

    def __init__(self, sliceSize, memorySize):
        self.counter = 0  # Counter to cycle time slices
        self.current = -1  # Current process (index of proc list)
        self.sliceSize = sliceSize  # Size of time slice
        self.procs = []  # List of scheduled processes

    def schedule(self, job):

    def update(self):
        self.counter += 1
        self.procs[self.current].time -= 1
        if self.counter == self.sliceSize:
            self.counter = 0
            self.current = (self.current + 1) % len(self.procs)