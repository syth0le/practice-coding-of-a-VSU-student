package main

import "fmt"

func main() {
	var amount int
	_, err := fmt.Scan(&amount)
	if err != nil {
		return
	}
	var array = make([]int, amount, amount)
	for i := 0; i < amount; i++ {
		_, err := fmt.Scan(&array[i])
		if err != nil {
			return
		}
	}
	var sum int
	for _, value := range array {
		if value > 0 {
			sum++
		}
	}
	fmt.Println(sum)

}
