package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(num int) bool {
	strNum := strconv.Itoa(num)
	length := len(strNum)
	for i := 0; i < length/2; i++ {
		if strNum[i] != strNum[length-i-1] {
			return false
		}
	}
	return true
}

func main() {
	var orderNum int
	_, err := fmt.Scan(&orderNum)
	if err != nil {
		return
	}
	var i int
	for {
		diffPlus := orderNum + i
		//diffMinus := math.Abs(float64(orderNum - i))
		if isPalindrome(diffPlus) {
			minValue := diffPlus - orderNum
			fmt.Println(minValue)
			break
		}
		//else if isPalindrome2(int(diffMinus)) {
		//	minValue := float64(orderNum) - diffMinus
		//	fmt.Println(minValue)
		//	break
		//}
		i++
	}
}
