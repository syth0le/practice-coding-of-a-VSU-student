package main

import "fmt"

//реализовать обобщение операции умножения для чисел и строк.
//Если первый аргумент функции — строка, то повторить её b раз, а если число, то вернуть a*b.

func Mul(a interface{}, b int) interface{} {
	switch val := a.(type) {
	case string:
		temp := ""
		for i := 0; i < b; i++ {
			temp += val
		}
		return temp
	default:
		return val.(int) * b
	}
}

func main() {
	fmt.Println(Mul("STR", 3))
	fmt.Println(Mul(3, 3))
}
