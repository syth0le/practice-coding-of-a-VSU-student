package main

import (
	"fmt"
	"sort"
)

type myStruct struct {
	n string
	f string
	s string
}

type Ascending []byte

func (s Ascending) Len() int           { return len(s) }
func (s Ascending) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Ascending) Less(i, j int) bool { return s[i] < s[j] }

type Descending []byte

func (s Descending) Len() int           { return len(s) }
func (s Descending) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }
func (s Descending) Less(i, j int) bool { return s[i] > s[j] }

func main() {
	var n int
	fmt.Scan(&n)
	inpStr := make([]myStruct, n, n)
	for i := 0; i < n; i++ {
		var mstr myStruct
		fmt.Scan(&mstr.n)
		fmt.Scan(&mstr.f)
		fmt.Scan(&mstr.s)
		inpStr[i] = mstr
	}

	for _, val := range inpStr {
		f := []byte(val.f)
		s := []byte(val.s)
		sort.Sort(Ascending(f))
		sort.Sort(Descending(s))
		val.f = string(f)
		val.s = string(s)

		if val.f < val.s {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
