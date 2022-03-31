package main

import "fmt"

/*
INSTEAD OF THIS USE iota
const (
	Sunday    = 0
	Monday    = 1
	Tuesday   = 2
	Wednesday = 3
	Thursday  = 4
	Friday    = 5
	Saturday  = 6
)
*/
const (
	Sunday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	_ // skip 7
	Finish
)

func main() {
	fmt.Println(Sunday)   // output 0
	fmt.Println(Saturday) // output 6
	fmt.Println(Finish)   // output 8

	const (
		u         = iota * 42 // u == 0 (индекс - 0, поэтому 0 * 42 = 0)
		v float64 = iota * 42 // v == 42.0 (индекс - 1, поэтому 1.0 * 42 = 42.0)
		w         = iota * 42 // w == 84  (индекс - 2, поэтому 2 * 42 = 84)
	)

	// переменные ни в одном блоке const, поэтому индекс не увеличился
	const x = iota // x == 0
	const y = iota // y == 0
}
