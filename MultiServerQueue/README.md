# MultiServerQueue
Single producer/multiple consumer queue implementation that reads input from stdin and generates a wordcount using multiple consumer threads.

## Building
This project is built in [Go](https://golang.org/) and can be built with the included makefile using `make`.

## Usage
After building the program can be run with:

`./msqueue <consumers>`

Where \<consumers\> is the number of worker threads to be created and input is read from stdin.

## Additional Information
