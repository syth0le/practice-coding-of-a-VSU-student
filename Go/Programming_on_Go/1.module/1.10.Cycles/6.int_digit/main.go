package main

import "fmt"

func main() {

	for {
		var num int
		_, err := fmt.Scan(&num)
		if err != nil {
			return
		}
		if num < 10 {
			continue
		} else if num > 100 {
			break
		} else {
			fmt.Println(num)
		}
	}

}
