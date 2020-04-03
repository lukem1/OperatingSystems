//
// msqueue.go
//
// Luke McGuire
// Matt Walter
//
// 2 April 2020
//
// counts the number of words in a given text file
// `go run msqueue.go ( Number of Go Routines) < random.txt `

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

var wordCount int = 0  // Total word count
var lock sync.Mutex  // Mutex lock to restrict write access to wordCount

func task(number int, c chan string, w *sync.WaitGroup) {
	taskWc := 0  // Local word count
	// While the channel is open process lines
	for line := range c {
		fmt.Printf("Task %d: %s\n", number, line)
		// Count words
		split := strings.Split(line, " ")
		for _, w := range split {
			if w != "" { // ignore empty strings
				taskWc += 1
			}
		}
	}

	// Update the total word count
	lock.Lock()
	wordCount += taskWc
	defer lock.Unlock()
	defer w.Done()
}

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: ./msqueue <consumers>\n")
		os.Exit(0)
	}
	consumers, _ := strconv.Atoi(os.Args[1])

	// Initialize channel to pass data to tasks
	c := make(chan string)
	// Initialize waitgroup to signal main when all tasks terminate
	var w sync.WaitGroup
	// Create the specified number of tasks
	for i := 0; i < consumers; i++ {
		w.Add(1)
		go task(i, c, &w)
	}

	// Initialize scanner to read from stdin
	scanner := bufio.NewScanner(os.Stdin)
	// Pass each line of the input to tasks via the channel
	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		c <- scanner.Text()
	}

	// Close the channel
	close(c)

	// Wait for tasks to terminate
	w.Wait()

	fmt.Printf("Total Word Count: %d\n", wordCount)

}
