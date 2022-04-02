package main

import (
	"fmt"
	"sort"
	"strconv"
)

func mixer(data []int) []int {
	var result []int
	for i := range data {
		for j := range data {
			var p int
			if j == i {
				continue
			}
			p = 3 - i - j
			tempString := fmt.Sprintf("%d%d%d", data[i], data[j], data[p])
			tempInt, _ := strconv.Atoi(tempString)
			result = append(result, tempInt)
		}
	}
	return result
}

func main() {
	var inputData int
	_, err := fmt.Scan(&inputData)
	if err != nil {
		return
	}
	var dataSlice []int
	for _, elem := range strconv.Itoa(inputData) {
		temp, _ := strconv.Atoi(string(elem))
		dataSlice = append(dataSlice, temp)
	}
	shuffledData := mixer(dataSlice)
	sort.Ints(shuffledData)
	for _, elem := range shuffledData {
		fmt.Println(elem)
	}

}
