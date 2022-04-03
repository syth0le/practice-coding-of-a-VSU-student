package main

import (
	"fmt"
	"math"
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
func isPalindrome2(num int) bool {
	str := strconv.Itoa(num)
	reversedStr := ""
	for i := len(str) - 1; i >= 0; i-- {
		reversedStr += string(str[i])
	}
	for i := range str {
		if str[i] != reversedStr[i] {
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
	var minValue = float64(orderNum)
	for {
		if isPalindrome2(i) {
			diff := math.Abs(float64(orderNum - i))
			if diff > minValue {
				fmt.Println(int(minValue))
				break
			} else {
				minValue = diff
			}
		}
		i++
	}
}
