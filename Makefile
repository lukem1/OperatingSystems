all: ptree

clean:
	rm ptree
	
ptree: ptree.c
	gcc -Wall -o ptree ptree.c
