package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	var n, d int
	_, err := fmt.Scan(&n, &d)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println(strings.Replace(strconv.Itoa(n), strconv.Itoa(d), "", -1))
}
