package main

import "fmt"

func main() {
	var array = make([]int, 3, 3)
	var a int
	for idx := range array {
		_, err := fmt.Scan(&a)
		if err != nil {
			return
		}
		array[idx] = a * a
	}
	var condition = array[2] == array[1]+array[0]
	if condition {
		fmt.Println("Прямоугольный")
	} else {
		fmt.Println("Непрямоугольный")
	}

}
