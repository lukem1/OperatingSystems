package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: ./msqueue <consumers>\n")
		os.Exit(0)
	}
	fmt.Printf("argc: %d argv: %s\n", len(os.Args), os.Args)
}
