package main

import (
	"fmt"
)

func main() {
	var workArray [10]uint8

	for i := range workArray {
		_, err := fmt.Scan(&workArray[i])
		if err != nil {
			return
		}
	}

	var ind1, ind2 uint
	for i := 0; i < 3; i++ {
		_, err := fmt.Scan(&ind1, &ind2)
		if err != nil {
			return
		}
		workArray[ind1], workArray[ind2] = workArray[ind2], workArray[ind1]
	}

	for _, x := range workArray {
		fmt.Print(x, " ")
	}
}
