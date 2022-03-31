package main

import "fmt"

func main() {
	var a, b int
	_, err := fmt.Scan(&a, &b)
	if err != nil {
		return
	}
	var sum int
	for i := a; i <= b; i++ {
		sum += i
	}
	fmt.Println(sum)

}
