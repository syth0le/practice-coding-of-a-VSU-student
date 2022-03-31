package main

import "fmt"

func main() {
	var amount int
	_, err := fmt.Scan(&amount)
	if err != nil {
		return
	}
	var array = make([]int, amount, amount)
	var a int
	for i := 0; i < amount; i++ {
		_, err := fmt.Scan(&a)
		if err != nil {
			return
		}
		array[i] = a
	}
	fmt.Println(array[3])
}
