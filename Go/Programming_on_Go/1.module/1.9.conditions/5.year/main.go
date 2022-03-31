package main

import "fmt"

func main() {
	var year int
	_, err := fmt.Scan(&year)
	if err != nil {
		return
	}
	if year%400 == 0 {
		fmt.Println("YES")
	} else if year%4 == 0 && year%100 != 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
