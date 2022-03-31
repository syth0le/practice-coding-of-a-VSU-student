package main

import "fmt"

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}
	first, second, third := num/100, num/10%10, num%10
	if first == second || second == third || third == first {
		fmt.Println("NO")
	} else {
		fmt.Println("YES")
	}

}
