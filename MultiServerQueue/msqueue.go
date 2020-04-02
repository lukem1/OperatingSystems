//
// msqueue.go
//
// Luke McGuire
// Matt Walter
//
// 2 April 2020
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sync"
)

var word_count int = 0
var lock sync.Mutex

func task(number int, c chan string, w *sync.WaitGroup) {
	task_wc := 0
	for line := range c {
		fmt.Printf("Task %d: %s\n", number, line)
		task_wc += 1 // TODO: Remove, do actual word count
	}
	
	
	lock.Lock()
	word_count += task_wc
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
	
	fmt.Printf("Total Word Count: %d\n", word_count)
	
}
