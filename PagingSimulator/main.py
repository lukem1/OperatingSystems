#
# main.py
# OperatingSystems
#
# Luke McGuire
# Matt Walter
# 28 February 2020
#

import random
import sys
from components import *


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
    except:
        print("Usage: python3 main.py <memorysize> <pagesize> <jobs> <minrun> <maxrun> <minmem> <maxmem> <seed>")
        exit(1)

    random.seed(seed)

    # Generate Processes
        ## make a list of all jobs 
    
    jobs = []

    for i in range(0,numberOfJobs):
        mem = random.randint(minmem,maxmem)
        time = random.randint(minrun, maxrun)

        jobs.append(Process(i, mem, time))


    for job in jobs:
        job.selfPrint()

    # Generate Page Table

    table = PageTable(pagesize, memorysize)



    # Initialize Scheduler

    # Schedule Processes

    # Print Summary


if __name__ == "__main__":
    main()
