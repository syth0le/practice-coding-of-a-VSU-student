package main

import "fmt"

func main() {
	var array = make([]int, 2, 2)
	for i := 0; i < 2; i++ {
		_, err := fmt.Scan(&array[i])
		if err != nil {
			return
		}
	}
	fmt.Println(float64(array[0]+array[1]) / 2.0)
}
