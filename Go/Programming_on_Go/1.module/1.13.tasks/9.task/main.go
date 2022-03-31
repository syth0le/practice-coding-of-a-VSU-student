package main

import "fmt"

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}

	for n >= 10 {
		newN := 0
		for n > 0 {
			newN += n % 10
			n /= 10
		}
		n = newN
	}
	fmt.Println(n)
}
