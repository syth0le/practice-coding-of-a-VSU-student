package main

import "fmt"

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}
	var first = num / 100
	var second = num / 10 % 10
	var third = num % 10
	fmt.Printf("%d%d%d", third, second, first)
}
