package main

import "fmt"

func main() {
	var ticket int
	_, err := fmt.Scan(&ticket)
	if err != nil {
		return
	}
	first := ticket / 1000
	second := ticket % 1000
	if sum(second) == sum(first) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}

func sum(num int) int {
	sum := 0
	for num != 0 {
		sum += num % 10
		num /= 10
	}
	return sum
}
