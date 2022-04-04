package main

import (
	"fmt"
)

type MyStruct struct {
	amount int
	price float64
}

func main() {
	var a int
	var one, packages, box int
	var values = []MyStruct {
		MyStruct{amount: 384, price: 160},
		MyStruct{amount: 24, price: 11},
		MyStruct{amount: 1, price: 1},
	}

	fmt.Scan(&a)
	for _, value := range values {

		a = a % value.amount
		fmt.Println(a, value)
		if a / value.amount >= 1 {

		}
		//if a == 1 {
		//	fmt.Println("HERE")
		//	break
		//}
		//if a == 0 {
		//	break
		//}
	}

}
