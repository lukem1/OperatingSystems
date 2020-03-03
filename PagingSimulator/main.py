#
# main.py
# OperatingSystems
#
# Luke McGuire
# Matt Walter
# 28 February 2020
#

from components import *
import random
import sys


def main():
    # Process parameters

    try:
        memorysize = int(sys.argv[1])
        pagesize = int(sys.argv[2])
        numberOfJobs = int(sys.argv[3])
        minrun = int(sys.argv[4])
        maxrun = int(sys.argv[5])
        minmem = int(sys.argv[6])
        maxmem = int(sys.argv[7])
        seed = int(sys.argv[8])
    except IndexError:
        print("Usage: python3 main.py <memorysize> <pagesize> <jobs> <minrun> <maxrun> <minmem> <maxmem> <seed>")
        exit(1)

    if memorysize % pagesize != 0:
        print("! Memory size must be an even multiple of the page size")
        exit(1)

    random.seed(seed)

    # Generate Processes
        ## make a list of all jobs 
    
    jobs = []

    for i in range(0,numberOfJobs):
        mem = random.randint(minmem,maxmem)
        time = random.randint(minrun, maxrun)

        jobs.append(Process(i, mem, time))

    # Initialize Page Table

    table = PageTable(pagesize, memorysize)

    # Initialize Scheduler and schedule processes

    scheduler = RoundRobin(1, table)
    for j in jobs:
        j.arrival = 0
        scheduler.schedule(j)

    print("-----Initial Snapshot-----")
    scheduler.printer()
    print("--------------------------")
    
    # Run to Completion
    print("Beginning Simulation...")
    while scheduler.update():
        scheduler.printer()

    # Print Summary
    print("----------Summary----------")
    print("Final simulator state:")
    scheduler.printer()
    print("Job statistics:")
    for job in jobs:
        print("[Job %d] Arrival Time: %d, Start Time %d, End Time %d" % (job.pid, job.arrival, job.start, job.end))


if __name__ == "__main__":
    main()
