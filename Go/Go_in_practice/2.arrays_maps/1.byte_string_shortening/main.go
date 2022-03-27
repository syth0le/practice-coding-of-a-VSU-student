package main

import (
	"fmt"
)

func main() {
	var text string
	var width int
	fmt.Scanf("%s %d", &text, &width)

	// Возьмите первые `width` байт строки `text`,
	// допишите в конце `...` и сохраните результат
	// в переменную `res`
	// ...
	res := text

	if len(text) > width {
		runes := []rune(text)[:width]
		res = string(runes) + "..."
	}

	fmt.Println(res)
}