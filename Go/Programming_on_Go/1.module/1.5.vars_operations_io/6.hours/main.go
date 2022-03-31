package main

import "fmt"

func main() {
	var input int
	_, err := fmt.Scan(&input)
	if err != nil {
		return
	}
	hours := input / 30
	minutes := input % 30 * 2
	fmt.Printf("It is %d hours %d minutes.", hours, minutes)
}
