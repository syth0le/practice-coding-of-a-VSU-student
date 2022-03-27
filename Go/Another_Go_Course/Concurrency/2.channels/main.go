package main

import (
	"fmt"
	"time"
)

func out(from, to int, ch chan int) {
	for i:=from; i<=to; i++ {
		time.Sleep(50 * time.Millisecond)
		fmt.Println(i)
	}
	if from == 0 {
		ch <- 1
	} else {
		ch <- 2
	}

}

func main() {
	ch := make(chan int)

	go out(0, 5, ch)
	go out(6, 10, ch)

	fmt.Printf("Gorutine %v finished\n", <-ch)
	fmt.Printf("Gorutine %v finished\n", <-ch)
}