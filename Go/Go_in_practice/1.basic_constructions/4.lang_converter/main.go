package main

import (
	"fmt"
)

func main() {
	var code string
	fmt.Scan(&code)

	// определите полное название языка по его коду
	// и запишите его в переменную `lang`
	// ...
	var lang string
	switch code {
	case "en":
		lang = "English"
	case "ru", "rus":
		lang = "Russian"
	case "fr":
		lang = "French"
	default:
		lang = "Unknown"
	}

	fmt.Println(lang)
}