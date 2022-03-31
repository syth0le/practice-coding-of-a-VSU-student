package main

import "fmt"

func main() {
	array := [5]int{}
	var a int
	for i := 0; i < 5; i++ {
		_, err := fmt.Scan(&a)
		if err != nil {
			return
		}
		array[i] = a
	}
	var max = array[0]
	for _, value := range array {
		if value > max {
			max = value
		}
	}
	fmt.Println(max)
}
