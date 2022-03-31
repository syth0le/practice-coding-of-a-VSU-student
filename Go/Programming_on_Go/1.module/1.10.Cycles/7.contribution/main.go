package main

import "fmt"

func main() {
	var x, p, y int
	_, err := fmt.Scan(&x, &p, &y)
	if err != nil {
		return
	}

	var years = 1
	var i = x + (x/100)*p
	for i < y {
		diff := (float64(i) / 100.0) * float64(p)
		i = int(float64(i) + diff)
		years++
	}
	fmt.Println(years)
}
