package main

import "fmt"

func main() {
	var counter, amount int
	_, err := fmt.Scan(&amount)
	if err != nil {
		return
	}
	for i := 0; i < amount; i++ {
		var num int
		_, err := fmt.Scan(&num)
		if err != nil {
			return
		}
		if num == 0 {
			counter++
		}

	}
	fmt.Println(counter)
}
