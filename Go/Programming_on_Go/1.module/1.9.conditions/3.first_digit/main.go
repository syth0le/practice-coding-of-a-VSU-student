package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	var num int
	_, err := fmt.Scan(&num)
	if err != nil {
		return
	}
	digitsStr := strconv.Itoa(num)
	length := len(digitsStr) - 1
	amount := math.Pow(10, float64(length))
	fmt.Println(num / int(amount))
}
