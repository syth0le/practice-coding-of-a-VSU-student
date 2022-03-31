package main

import "fmt"

func main() {
	var a int
	_, err := fmt.Scan(&a)
	if err != nil {
		return
	}
	fmt.Println(a % 100 / 10)
}
