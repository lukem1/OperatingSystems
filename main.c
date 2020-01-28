#include <stdio.h>
#include <dirent.h>

// Structure to keep track of processes and their relationships
struct process
{
	int pid; // Process id
	int ppid; // Parent process id
	int vsize; // Size of virtual address space
	char exe[];
	
	struct process parent;
};
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
	char *a = *(argv + 1);
	printf("argv: %s\n", a);
	struct dirent *dir;
	
	printf("Number?: %d\n", isNumber(a));
	
	DIR *proc = opendir("/proc");
	
	/*while ((dir = readdir(proc)) != NULL)
	{
		printf("%s\n", dir->d_name);
	}*/
	
	closedir(proc);
	return 0;
}
