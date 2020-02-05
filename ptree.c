//
// ptree.c
//
// Luke McGuire
// Matt Walter
//
// 4 February 2020
//

#include <stdio.h>
#include <dirent.h>
#include <string.h>

// Structure to hold process information
struct process
{
	int pid; // Process ID
	int ppid; // Parent process ID
	unsigned long vsize; // Virtual address space size (bytes)
	char pname[32]; // Name of executable
};

// Recursivley prints the processes as a tree
void printTree(struct process list[], int size, int depth, int ppid)
{
	// Find processes with a parent process ID of ppid
	for (int i = 0; i < size; i++)
	{
		if (list[i].ppid == ppid)
		{
			for (int j = 0; j < depth; j++)
				printf("  ");
			printf("(%d) %s, %lu kb\n", list[i].pid, list[i].pname, list[i].vsize/1000);
			// Recursive call to find and print children of current process
			printTree(list, size, depth+1, list[i].pid); 
		}
	}
}

// Determines if a string is a number
// Built to identify processes in the proc dir
int isNumber(char s[])
{
	char digits[] = {'1','2','3','4','5','6','7','8','9','0'};
	for (int i = 0; s[i] != '\0'; i++)
	{
		int found = 0;
		for (int j = 0; j < sizeof(digits)/sizeof(digits[0]); j++)
		{
			if (s[i] == digits[j])
			{
				found = 1;
				break;
			}
		}
		if (!found) // Found non numeric character
		{
			return 0;
		}
	}
	return 1; // All numeric characters
}

int main(int argc, char *argv[])
{
	
	struct dirent *dir;
	
	// Read proc and count processes
	DIR *proc = opendir("/proc");
	int procCount = 0;
	while ((dir = readdir(proc)) != NULL)
	{
		if (isNumber(dir->d_name)) { procCount += 1; }
	}
	closedir(proc);
	
	// Array of processes sized based on counted processes
	struct process procList[procCount];
	
	// Read in process information and store in array
	int c = 0;
	proc = opendir("/proc");
	while ((dir = readdir(proc)) != NULL)
	{
		if (isNumber(dir->d_name))
		{ 
			int pid;
			char pname[32];
			int ppid;
			unsigned long vsize;
			char path[267];
			sprintf(path, "/proc/%s/stat", dir->d_name);
			FILE *stream = fopen(path, "r");
			// Scan /proc/pid/stat for process info
			fscanf(stream, "%d %s %*s %d %*d %*d %*d %*d %*u %*u %*u %*u %*u %*u %*u %*d %*d %*d %*d %*d %*d %*u %lu", &pid, pname, &ppid, &vsize);
			// Store process info in process struct in the array
			procList[c].pid = pid;
			procList[c].ppid = ppid;
			strcpy(procList[c].pname, pname);
			procList[c].vsize = vsize;
			c += 1;
		}
	}
	closedir(proc);
	
	// Call recursive function to print process tree
	printTree(procList, procCount, 0, 0);
	
	return 0;
}
