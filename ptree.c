#include <stdio.h>
#include <dirent.h>

// Structure to keep track of processes and their relationships
struct process_old
{
	int pid; // Process id
	int ppid; // Parent process id
	int vsize; // Size of virtual address space
	char **exe; // Pointer to name of exe TODO: may be incorrect type
	
	struct process *parent; // Pointer to parent
	struct process *children[]; // Array of pointers to children
};

struct process
{
	int pid;
	int ppid;
	unsigned long vsize;
	char **name;
	
	struct process *next;
	struct process *prev;
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
		if (!found)
		{
			//printf("Not Found: %c\n", s[i]);
			return 0;
		}
	}
	return 1;
}

int main(int argc, char *argv[])
{
	// TODO kb not bytes
	//char *a = *(argv + 1);
	//printf("argv: %s\n", a);
	//printf("Number?: %d\n", isNumber(a));
	
	struct dirent *dir;
	DIR *proc = opendir("/proc");
	
	while ((dir = readdir(proc)) != NULL)
	{
		if (isNumber(dir->d_name)) { 
			printf("Process: "); 
			printf("%s\n", dir->d_name);
			int pid;
			char *name[32];
			int ppid;
			unsigned long vsize;
			char path[267];
			sprintf(path, "/proc/%s/stat", dir->d_name);
			FILE *stream = fopen(path, "r");
			fscanf(stream, "%d %s %*s %d %*d %*d %*d %*d %*u %*u %*u %*u %*u %*u %*u %*d %*d %*d %*d %*d %*d %*u %lu", &pid, name, &ppid, &vsize);
			//fscanf(stream, "%d %s %*s %d ", &pid, name, &ppid);
			printf("pid: %d, ppid: %d, name: %s, memory: %lu (kb)\n", pid, ppid, name, vsize/1000);
		}
	}
	
	closedir(proc);
	return 0;
}
