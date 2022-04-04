package main

import (
	"fmt"
)

func modFact(n, p int) int {
	if n >= p {
		return 0
	}
	result := 1
	for i:=1; i<=n; i++ {
		result = (result * i) % p
	}
	return result
}

func main() {
	var pairs int
	fmt.Scan(&pairs)
	data := make([]int, pairs+1)

	var a, b int
	for i:=0; i<pairs+1; i++{
		fmt.Scan(&a, &b)
		data[i] = modFact(a, b)
		value := pairs - i
		defer func() { fmt.Println(data[value]) }()
	}
}
