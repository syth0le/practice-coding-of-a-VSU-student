package main

import "fmt"

func main() {
	var current, i, temp int
	for {
		_, err := fmt.Scan(&temp)
		if err != nil {
			return
		}
		if temp == 0 {
			break
		} else if current < temp {
			current = temp
			i = 1
		} else if current == temp {
			i++
		}
	}
	fmt.Println(i)
}
