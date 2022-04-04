package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	myscanner := bufio.NewScanner(os.Stdin)
	myscanner.Scan()
	line := myscanner.Text()
	array := strings.Split(line, " ")
	fmt.Printf("Квадрат со стороной %d\n", len(array))
	for i := 0; i<len(array); i++ {
		fmt.Println(line)
	}
}
