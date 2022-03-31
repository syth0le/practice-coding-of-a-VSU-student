package main

import "fmt"

func main() {
	var amount, min int
	var counter = 1
	_, err := fmt.Scan(&amount)
	if err != nil {
		return
	}
	var num int
	_, err = fmt.Scan(&num)
	if err != nil {
		return
	}
	min = num
	for i := 0; i < amount-1; i++ {
		var num int
		_, err = fmt.Scan(&num)
		if err != nil {
			return
		}
		if num == min {
			counter++
		}
		if num < min {
			min = num
			counter = 1
		}

	}
	fmt.Println(counter)
}
