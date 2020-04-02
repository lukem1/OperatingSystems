package main

import (
	"fmt"
	"os"
	"bufio"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: ./msqueue <consumers>\n")
		os.Exit(0)
	}
	fmt.Printf("argc: %d argv: %s\n", len(os.Args), os.Args)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
