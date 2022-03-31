package main

import "fmt"

func main() {

	var a, b, c int
	_, err := fmt.Scan(&a)
	if err != nil {
		return
	}
	_, err = fmt.Scan(&b)
	if err != nil {
		return
	}

	a = a * a
	b = b * b
	c = a + b
	fmt.Println(c)
}
