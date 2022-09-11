package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var amountTest int
	fmt.Fscan(in, &amountTest)

	for t := 0; t < amountTest; t++ {

		var lenList int
		fmt.Fscan(in, &lenList)

		graph := make(map[int][2]int, lenList)

		parent := 0
		for n := 0; n < lenList; n++ {
			var vert, a, b int
			fmt.Fscan(in, &vert, &a, &b)

			graph[vert] = [2]int{a, b}
			parent = vert
		}

		son := graph[parent][0]

		sonSlice := make([]int, lenList/2)

		l := 0

		// расмотрим lenList/2 вершин
		for i := 0; i < lenList; i++ {
			if i < lenList/2 {
				sonSlice[i] = parent
			}

			if i >= lenList/2 {
				fmt.Fprintf(out, "%v %v\n", sonSlice[l], parent)
				l++
			}

			if graph[son][0] != parent {
				parent = son
				son = graph[son][0]
			} else {
				parent = son
				son = graph[son][1]
			}

		}
		fmt.Fprintln(out)

	}

}