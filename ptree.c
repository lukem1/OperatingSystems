#include <stdio.h>
#include <dirent.h>

// Structure to hold process data
struct process
{
	int pid;
	int ppid;
	unsigned long vsize;
	char **pname;
};

// Prints a list of proccess structs
void printList(struct process list[], int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("pid: %d, ppid: %d, name: %s, memory: %lu (kb)\n", list[i].pid, list[i].ppid, list[i].pname, list[i].vsize/1000);
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
	
	int procCount = 0;
	while ((dir = readdir(proc)) != NULL)
	{
		if (isNumber(dir->d_name)) { procCount += 1; }
	}
	closedir(proc);
	
	struct process procList[procCount];
	
	int c = 0;
	proc = opendir("/proc");
	while ((dir = readdir(proc)) != NULL)
	{
		if (isNumber(dir->d_name)) { 
			//printf("Process: %s\n", dir->d_name); 
			int pid;
			char *pname[32];
			int ppid;
			unsigned long vsize;
			char path[267];
			sprintf(path, "/proc/%s/stat", dir->d_name);
			FILE *stream = fopen(path, "r");
			fscanf(stream, "%d %s %*s %d %*d %*d %*d %*d %*u %*u %*u %*u %*u %*u %*u %*d %*d %*d %*d %*d %*d %*u %lu", &pid, pname, &ppid, &vsize);
			printf("pid: %d, ppid: %d, name: %s, memory: %lu (kb)\n", pid, ppid, pname, vsize/1000);
			procList[c].pid = pid;
			procList[c].ppid = ppid;
			procList[c].pname = pname;
			procList[c].vsize = vsize;
			c += 1;
		}
	}
	printf("Head of process list:\n");
	printf("pid: %d, ppid: %d, name: %s, memory: %lu (kb)\n", procList[0].pid, procList[0].ppid, procList[0].pname, procList[0].vsize/1000);
	printList(procList, procCount);
	closedir(proc);
	return 0;
}
