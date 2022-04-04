package main

import (
	"fmt"
)

func Algorithm(n, p int) int {
	return p
}

func main() {
	var pairs int
	fmt.Scan(&pairs)
	data := make([]int, pairs)

	var a, b int
	for i:=0; i<pairs; i++{
		fmt.Scan(&a, &b)
		data[i] = Algorithm(a, b)
		value := (pairs - 1) - i
		defer func() { fmt.Println(data[value]) }()
	}
}
