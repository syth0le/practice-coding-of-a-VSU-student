package main

import "fmt"

func fib(n int) int {
	a := 1
	b := 1
	for i := 0; i < n; i++ {
		a, b = b, b+a
	}
	return a
}

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}
	res := 0
	for i := 1; i <= num*2; i++ {
		res = fib(i)
		if res == num {
			fmt.Println(i + 1)
			return
		}
		if res > num {
			break
		}
	}
	fmt.Println(-1)

}
