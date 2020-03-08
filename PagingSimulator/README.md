# PagingSimulator
Simulator that implements a Round Robin shceduler and memory management via paging

## Usage
`python3 main.py <memorysize> <pagesize> <jobs> <minrun> <maxrun> <minmem> <maxmem> <seed>`

The memory size must be an even multiple of the page size

## Additional Information

### Notable Implementation Details

#### Handling Memory Shortages

When attempting to schedule a job that requires more memory than there is available the scheduler will 
place the job in a queue of jobs waiting for memory, and each time memory is freed the queue will be checked
for jobs that can fit in the newley available space.

### Output Details

For each simulated second the simulator prints out the following information:
- The current simulator time
- The currently running job
- The queue of jobs waiting for sufficient memory to be freed
- The list of jobs that are currently scheduled 
- The page table
- Any jobs that have completed

After the simulator completes the following summary information is also printed for each job:
- Arrival time
- Start time
- End time
