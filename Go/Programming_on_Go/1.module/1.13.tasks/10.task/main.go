package main

import "fmt"

func main() {
	var a, b int
	var isFound bool
	_, err := fmt.Scan(&a, &b)
	if err != nil {
		return
	}

	for i := b; i >= a; i-- {
		if i%7 == 0 {
			fmt.Println(i)
			isFound = true
			break
		}
	}
	if !isFound {
		fmt.Println("NO")
	}
}
