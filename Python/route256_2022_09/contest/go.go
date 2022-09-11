package main

import (
	"bufio"
	"fmt"
	"os"
)

type Start struct {
	x, y int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var amountTest int
	fmt.Fscan(in, &amountTest)

	for t := 0; t < amountTest; t++ {

		// кол-во строк и столбцов
		var lines, columns int
		fmt.Fscan(in, &lines, &columns)

		// слайс для хранения рамок
		//frameBox := make([]*frame, 0)

		mtrx := make([][]byte, lines+2)
		start := Start{}

		// заполним матрицу и найдем углы рамок
		// у матрицы будет рамка, состоящая из точек
		for i := 0; i < lines+2; i++ {
			mtrx[i] = make([]byte, columns+2)

			var elem []byte
			if i != 0 && i != lines+1 {
				fmt.Fscan(in, &elem)
			}

			for j := 0; j < columns+2; j++ {
				// создаем рамку из точек
				if j == 0 || j == columns+1 || i == 0 || i == lines+1 {
					mtrx[i][j] = '.'
					continue
				}

				mtrx[i][j] = elem[j-1]

				/*if mtrx[i][j] == '*' && (mtrx[i-1][j] == '*' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '*' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '*' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '*') {
					// значит это начало
					start.x = i
					start.y = j
				}*/
			}
		}

		for i := 1; i < lines+1; i++ {
			for j := 1; j < columns+1; j++ {
				if mtrx[i][j] == '*' && (mtrx[i-1][j] == '*' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '*' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '*' && mtrx[i][j+1] == '.') || (mtrx[i-1][j] == '.' && mtrx[i+1][j] == '.' && mtrx[i][j-1] == '.' && mtrx[i][j+1] == '*') {
					// значит это начало
					start.x = i
					start.y = j
				}
			}
		}

		//fmt.Fprintln(out, start)
		End := start
		// двигаемся от начала
		for {
			if mtrx[start.x-1][start.y] == '*' && (start.x-1 != End.x || start.y != End.y) {
				// значит влево
				fmt.Fprint(out, "U")
				End.x = start.x
				End.y = start.y
				start.x--
			} else if mtrx[start.x+1][start.y] == '*' && !(start.x+1 == End.x && start.y == End.y) {
				// значит вправо
				fmt.Fprint(out, "D")
				End.x = start.x
				End.y = start.y
				start.x++
			} else if mtrx[start.x][start.y-1] == '*' && (start.y-1 != End.y || start.x != End.x) {
				// значит вправо
				fmt.Fprint(out, "L")
				End.x = start.x
				End.y = start.y
				start.y--
			} else if mtrx[start.x][start.y+1] == '*' && (start.y+1 != End.y || start.x != End.x) {
				// значит вправо
				fmt.Fprint(out, "R")
				End.x = start.x
				End.y = start.y
				start.y++
			} else {
				break
			}
			//	fmt.Fprintln(out, start)
			//fmt.Fprintln(out, End)
		}
		fmt.Fprintln(out)
	}
}