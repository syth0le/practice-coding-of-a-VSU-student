package main

import "fmt"

func main() {
	var seconds int
	_, err := fmt.Scan(&seconds)
	if err != nil {
		return
	}
	var hours = seconds / 3600
	var minutes = seconds % 3600 / 60
	fmt.Printf("It is %d hours %d minutes.", hours, minutes)
}
