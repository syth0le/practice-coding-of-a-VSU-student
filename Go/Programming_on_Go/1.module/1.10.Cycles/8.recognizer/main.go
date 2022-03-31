package main

import "fmt"

func main() {
	var a, b string
	_, err := fmt.Scan(&a, &b)
	if err != nil {
		return
	}

	for _, a1 := range a {
		for _, b1 := range b {
			if a1 == b1 {
				fmt.Print(string(a1) + " ")
			}
		}
	}
}
