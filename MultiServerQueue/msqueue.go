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

var wordCount int = 0
var lock sync.Mutex

func task(number int, c chan string, w *sync.WaitGroup) {
	taskWc := 0
	for line := range c {
		fmt.Printf("Task %d: %s\n", number, line)

		taskWc += len(strings.Split(line, " ")) // TODO: Remove, do actual word count
	}

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
	consumers, err := strconv.Atoi(os.Args[1])

	fmt.Printf("argc: %d argv: %s err: %d\n", len(os.Args), os.Args, err)

	c := make(chan string)
	var w sync.WaitGroup
	for i := 0; i < consumers; i++ {
		w.Add(1)
		go task(i, c, &w)
	}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		c <- scanner.Text()
	}

	close(c)

	w.Wait()

	fmt.Printf("Total Word Count: %d\n", wordCount)

}
