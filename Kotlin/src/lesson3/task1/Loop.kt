@file:Suppress("UNUSED_PARAMETER")

package lesson3.task1

import java.lang.Math.pow
import kotlin.math.sqrt

/**
 * Пример
 *
 * Вычисление факториала
 */
fun factorial(n: Int): Double {
    var result = 1.0
    for (i in 1..n) {
        result = result * i // Please do not fix in master
    }
    return result
}

/**
 * Пример
 *
 * Проверка числа на простоту -- результат true, если число простое
 */
fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    if (n == 2) return true
    if (n % 2 == 0) return false
    for (m in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % m == 0) return false
    }
    return true
}

/**
 * Пример
 *
 * Проверка числа на совершенность -- результат true, если число совершенное
 */
fun isPerfect(n: Int): Boolean {
    var sum = 1
    for (m in 2..n / 2) {
        if (n % m > 0) continue
        sum += m
        if (sum > n) break
    }
    return sum == n
}

/**
 * Пример
 *
 * Найти число вхождений цифры m в число n
 */
fun digitCountInNumber(n: Int, m: Int): Int =
    when {
        n == m -> 1
        n < 10 -> 0
        else -> digitCountInNumber(n / 10, m) + digitCountInNumber(n % 10, m)
    }

/**
 * Простая
 *
 * Найти количество цифр в заданном числе n.
 * Например, число 1 содержит 1 цифру, 456 -- 3 цифры, 65536 -- 5 цифр.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
fun digitNumber(n: Int): Int {
    var temp = n
    var i = 1
    while (true) {
        temp /= 10
        if (temp == 0) return i
        i++
    }
}

/**
 * Простая
 *
 * Найти число Фибоначчи из ряда 1, 1, 2, 3, 5, 8, 13, 21, ... с номером n.
 * Ряд Фибоначчи определён следующим образом: fib(1) = 1, fib(2) = 1, fib(n+2) = fib(n) + fib(n+1)
 */
fun fib(n: Int): Int {
    var temp = n
    var rez = 1
    var rez2 = 1
    for (i in 2 until n) {
        temp--
        rez += rez2
        rez2 = rez - rez2
    }
    return rez
}

//fun main() {
//    println(fib(6))}


/**
 * Простая
 *
 * Для заданных чисел m и n найти наименьшее общее кратное, то есть,
 * минимальное число k, которое делится и на m и на n без остатка
 */
fun lcm(m: Int, n: Int): Int {
    var m = m
    var n = n
    val temp = m * n
    while (m != 0 && n != 0) {
        if (m > n) {
            m %= n
        } else n %= m
    }
    return temp / (n + m)
}

/**
 * Простая
 *
 * Для заданного числа n > 1 найти минимальный делитель, превышающий 1
 */
fun minDivisor(n: Int): Int {
    for (i in 2..sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) {
            return i
        }
    }
    return n
}

/**
 * Простая
 *
 * Для заданного числа n > 1 найти максимальный делитель, меньший n
 */
fun maxDivisor(n: Int): Int = n / minDivisor(n)

/**
 * Простая
 *
 * Определить, являются ли два заданных числа m и n взаимно простыми.
 * Взаимно простые числа не имеют общих делителей, кроме 1.
 * Например, 25 и 49 взаимно простые, а 6 и 8 -- нет.
 */
fun isCoPrime(m: Int, n: Int): Boolean = (m * n) / lcm(m, n) == 1

/**
 * Простая
 *
 * Для заданных чисел m и n, m <= n, определить, имеется ли хотя бы один точный квадрат между m и n,
 * то есть, существует ли такое целое k, что m <= k*k <= n.
 * Например, для интервала 21..28 21 <= 5*5 <= 28, а для интервала 51..61 квадрата не существует.
 */
fun squareBetweenExists(m: Int, n: Int): Boolean {
    val rm = m.toDouble()
    val rn = n.toDouble()
    var ri = 0.0
    for (i in 1..m) {
        ri = pow(i.toDouble(), 2.0)
        if (ri in rm..rn) return true
    }
    return false
}
//fun main(){
//    print(squareBetweenExists(152374337,152423715)) }

/**
 * Средняя
 *
 * Гипотеза Коллатца. Рекуррентная последовательность чисел задана следующим образом:
 *
 *   ЕСЛИ (X четное)
 *     Xслед = X /2
 *   ИНАЧЕ
 *     Xслед = 3 * X + 1
 *
 * например
 *   15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 4 2 1 4 2 1 ...
 * Данная последовательность рано или поздно встречает X == 1.
 * Написать функцию, которая находит, сколько шагов требуется для
 * этого для какого-либо начального X > 0.
 */
fun collatzSteps(x: Int): Int {
    var temp = x
    var count = 0
    while (temp != 1) {
        if (temp % 2 == 0) {
            temp /= 2
            count++
        } else {
            temp = 3 * temp + 1
            count++
        }
    }
    return count
}


/**
 * Средняя
 *
 * Поменять порядок цифр заданного числа n на обратный: 13478 -> 87431.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
fun revert(n: Int): Int {
    var rez = 0
    var temp = n
    var num = 0
    while (temp != 0) {
        num = temp % 10
        rez *= 10
        rez += num
        temp /= 10
    }
    return rez
}

//fun main(){
//    println(revert(13457))}
/**
 * Средняя
 *
 * Проверить, является ли заданное число n палиндромом:
 * первая цифра равна последней, вторая -- предпоследней и так далее.
 * 15751 -- палиндром, 3653 -- нет.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
fun isPalindrome(n: Int): Boolean = revert(n) == n

//fun main(){
//    println(isPalindrome(13431))}

/**
 * Средняя
 *
 * Для заданного числа n определить, содержит ли оно различающиеся цифры.
 * Например, 54 и 323 состоят из разных цифр, а 111 и 0 из одинаковых.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
fun hasDifferentDigits(n: Int): Boolean {
    var numReal = n / 10
    while (numReal > 0) {
        if (numReal % 10 != n % 10) return true
        else numReal /= 10
    }
    return false
}

//fun main(){
//    println(false == hasDifferentDigits(111111)) }
/**
 * Сложная
 *
 * Найти n-ю цифру последовательности из квадратов целых чисел:
 * 149162536496481100121144...
 * Например, 2-я цифра равна 4, 7-я 5, 12-я 6.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
fun squareSequenceDigit(n: Int): Int {
    var current = 0
    var temp = 0
    var count = 0
    var countRez = 0
    var tempNum = 0
    var rezCount = 0
    for (i in 1..n) {
        temp = i * i
        current = temp
        while (temp != 0) {
            temp /= 10
            count++
        }
        countRez += count
        if (n <= countRez) {
            tempNum = current
            rezCount = countRez - n
            if (rezCount == 0) {
                tempNum %= 10
            } else {
                tempNum /= pow(10.0, rezCount.toDouble()).toInt()
                tempNum %= 10
            }
            return tempNum
        }
        count = 0
    }
    return tempNum
}

//fun main() {
//    println(squareSequenceDigit(17))}

/**
 * Сложная
 *
 * Найти n-ю цифру последовательности из чисел Фибоначчи (см. функцию fib выше):
 * 1123581321345589144...
 * Например, 2-я цифра равна 1, 9-я 2, 14-я 5.
 *
 * Использовать операции со строками в этой задаче запрещается.
 */
//fun main() {
//    println(fibSequenceDigit(9))}

fun fibSequenceDigit(n: Int): Int {
    var current = 0
    var temp = 0
    var count = 0
    var countRez = 0
    var tempNum = 0
    var rezCount = 0
    for (i in 1..n) {
        temp = fib(i)
        current = temp
        while (temp != 0) {
            temp /= 10
            count++
        }
        countRez += count
        if (n <= countRez) {
            tempNum = current
            rezCount = countRez - n
            if (rezCount == 0) {
                tempNum %= 10
            } else {
                tempNum /= pow(10.0, rezCount.toDouble()).toInt()
                tempNum %= 10
            }
            return tempNum
        }
        count = 0
    }
    return tempNum
}
