package main

import "fmt"

func main() {
	var a int = 8
	const b int = 10
	a = a + b
	//b = b + a cannot do that
	fmt.Println(a)
}
