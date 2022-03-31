package main

import "fmt"

func main() {
	var array = make([]int, 3, 3)
	for idx := range array {
		_, err := fmt.Scan(&array[idx])
		if err != nil {
			return
		}
	}

	var condition = array[0]+array[1] > array[2] && array[1]+array[2] > array[0] && array[2]+array[0] > array[1]
	if condition {
		fmt.Println("Существует")
	} else {
		fmt.Println("Не существует")
	}

}
