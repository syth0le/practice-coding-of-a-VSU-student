package main

import "fmt"

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}

	for i := 1; i <= num; i++ {
		res := 1
		for j := 1; j < i; j++ {
			res *= 2
		}
		if res > num {
			break
		}
		fmt.Print(res, " ")
	}

}
