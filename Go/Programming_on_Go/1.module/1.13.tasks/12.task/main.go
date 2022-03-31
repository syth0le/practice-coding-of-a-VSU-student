package main

import "fmt"

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}

	for i := 0; i < num; i++ {
		res := i * i
		if res > num {
			break
		}
		fmt.Println(res)
	}

}
