package main

import "fmt"

func main() {
	var phoneNumber int
	_, err := fmt.Scan(&phoneNumber)
	if err != nil {
		return
	}
	var code = phoneNumber % 10000000000 / 10000000
	fmt.Println(code)
}
