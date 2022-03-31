package main

import "fmt"

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}

	fmt.Printf("%b", n)
}
