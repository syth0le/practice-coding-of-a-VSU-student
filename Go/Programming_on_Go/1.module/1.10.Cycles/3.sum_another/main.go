package main

import "fmt"

func main() {
	var n, num int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}

	sum := 0
	for i := 0; i < n; i++ {
		_, err := fmt.Scan(&num)
		if err != nil {
			return
		}

		if num >= 10 && num < 100 && num%8 == 0 {
			sum += num
		}
	}
	fmt.Println(sum)
}
