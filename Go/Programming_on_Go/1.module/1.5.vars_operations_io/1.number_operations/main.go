package main

import "fmt"

func main() {
	var a int
	_, err := fmt.Scan(&a)
	if err != nil {
		return
	}
	a *= 2
	a += 100
	fmt.Println(a)
}
