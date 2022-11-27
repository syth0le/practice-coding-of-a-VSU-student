package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strings"
	"unicode"
)

//Напишите функцию MyCheck(input string) error, которая должна проверять строку на соответствие следующим параметрам:
//- Строка не должна содержать цифр (found numbers).
//- Длина должна быть меньше 20 символов (line is too long).
//- Строка должна иметь два пробела (no two spaces).
//В скобках приведены тексты возвращаемых ошибок.
//Функция должна находить все возможные ошибки за один вызов.Результат должен содержать слайс ошибок,
//по которым строка не прошла проверку, или быть nil.Подсказка: определите свой тип для слайса ошибок.

// 1) вставьте определение типа для []error
// 2) определите метод Error для вашего типа, который будет выводить
//    все ошибки слайса
// 3) реализуйте функцию MyCheck
//
// ...

type Errors []error

func (errs Errors) Error() string {
	var out string
	for _, err := range errs {
		out += err.Error() + ";"
	}
	return strings.TrimRight(out, `;`)
}

func MyCheck(s string) error {
	var (
		spaces         int
		isNumbersThere bool
		errs           Errors
	)

	if len([]rune(s)) > 20 {
		errs = Errors{errors.New(`line is too long`)}
	}
	for _, c := range s {
		if c == ' ' {
			spaces++
		}
		if unicode.IsDigit(c) {
			isNumbersThere = true
		}
	}
	if spaces != 2 {
		errs = append(errs, errors.New("no two spaces"))
	}
	if isNumbersThere {
		errs = append(errs, errors.New("found numbers"))
	}
	if len(errs) != 0 {
		return errs
	}
	return nil
}

func main() {
	for {
		fmt.Printf("Укажите строку (q для выхода): ")
		reader := bufio.NewReader(os.Stdin)
		ret, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println(err)
			continue
		}
		ret = strings.TrimRight(ret, "\n")
		if ret == `q` {
			break
		}
		if err = MyCheck(ret); err != nil {
			fmt.Println(err)
		} else {
			fmt.Println(`Строка прошла проверку`)
		}
	}
}
