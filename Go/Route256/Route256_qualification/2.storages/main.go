package main

import "fmt"

type MyStruct struct {
	max int
	idx int
}

func Max(data []int) MyStruct {
	max := MyStruct{max:data[0], idx: 0}
	for i, value := range data {
		if max.max < value {
			max = MyStruct{max: value, idx: i}
		}
	}
	return max
}

func main() {
	var amount, sum int
	fmt.Scan(&amount)
	data := make([]int, amount)
	for i:=0; i<amount; i++ {
		fmt.Scan(&data[i])
	}

	res := Max(data)
	sum += res.max * (res.idx + 1)
	for {
		if len(data[res.idx:]) == 1 {
			break
		}
		data = data[res.idx+1:]
		res = Max(data)
		sum += res.max * (res.idx + 1)
		if len(data) == 0 {
			break
		}
	}
	fmt.Println(sum)
}
