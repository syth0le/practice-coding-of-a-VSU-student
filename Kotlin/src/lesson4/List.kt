@file:Suppress("UNUSED_PARAMETER", "ConvertCallChainIntoSequence")

package lesson4.task1

import lesson1.task1.discriminant
import java.lang.Math.pow
import kotlin.math.sqrt
import lesson3.task1.minDivisor

/**
 * Пример
 *
 * Найти все корни уравнения x^2 = y
 */
fun sqRoots(y: Double) =
    when {
        y < 0 -> listOf()
        y == 0.0 -> listOf(0.0)
        else -> {
            val root = sqrt(y)
            // Результат!
            listOf(-root, root)
        }
    }

/**
 * Пример
 *
 * Найти все корни биквадратного уравнения ax^4 + bx^2 + c = 0.
 * Вернуть список корней (пустой, если корней нет)
 */
fun biRoots(a: Double, b: Double, c: Double): List<Double> {
    if (a == 0.0) {
        return if (b == 0.0) listOf()
        else sqRoots(-c / b)
    }
    val d = discriminant(a, b, c)
    if (d < 0.0) return listOf()
    if (d == 0.0) return sqRoots(-b / (2 * a))
    val y1 = (-b + sqrt(d)) / (2 * a)
    val y2 = (-b - sqrt(d)) / (2 * a)
    return sqRoots(y1) + sqRoots(y2)
}

/**
 * Пример
 *
 * Выделить в список отрицательные элементы из заданного списка
 */
fun negativeList(list: List<Int>): List<Int> {
    val result = mutableListOf<Int>()
    for (element in list) {
        if (element < 0) {
            result.add(element)
        }
    }
    return result
}

/**
 * Пример
 *
 * Изменить знак для всех положительных элементов списка
 */
fun invertPositives(list: MutableList<Int>) {
    for (i in 0 until list.size) {
        val element = list[i]
        if (element > 0) {
            list[i] = -element
        }
    }
}

/**
 * Пример
 *
 * Из имеющегося списка целых чисел, сформировать список их квадратов
 */
fun squares(list: List<Int>) = list.map { it * it }

/**
 * Пример
 *
 * Из имеющихся целых чисел, заданного через vararg-параметр, сформировать массив их квадратов
 */
fun squares(vararg array: Int) = squares(array.toList()).toTypedArray()

/**
 * Пример
 *
 * По заданной строке str определить, является ли она палиндромом.
 * В палиндроме первый символ должен быть равен последнему, второй предпоследнему и т.д.
 * Одни и те же буквы в разном регистре следует считать равными с точки зрения данной задачи.
 * Пробелы не следует принимать во внимание при сравнении символов, например, строка
 * "А роза упала на лапу Азора" является палиндромом.
 */
fun isPalindrome(str: String): Boolean {
    val lowerCase = str.toLowerCase().filter { it != ' ' }
    for (i in 0..lowerCase.length / 2) {
        if (lowerCase[i] != lowerCase[lowerCase.length - i - 1]) return false
    }
    return true
}

/**
 * Пример
 *
 * По имеющемуся списку целых чисел, например [3, 6, 5, 4, 9], построить строку с примером их суммирования:
 * 3 + 6 + 5 + 4 + 9 = 27 в данном случае.
 */
fun buildSumExample(list: List<Int>) = list.joinToString(separator = " + ", postfix = " = ${list.sum()}")

/**
 * Простая
 *
 * Найти модуль заданного вектора, представленного в виде списка v,
 * по формуле abs = sqrt(a1^2 + a2^2 + ... + aN^2).
 * Модуль пустого вектора считать равным 0.0.
 */
fun abs(v: List<Double>): Double = sqrt(v.foldRight(0.0) { acc, it -> acc * acc + it })

/**
 * Простая
 *
 * Рассчитать среднее арифметическое элементов списка list. Вернуть 0.0, если список пуст
 */
fun mean(list: List<Double>): Double = if (list.isEmpty()) 0.0 else list.fold(0.0) { acc, it -> acc + it } / list.size
//fun mean(list: List<Double>): Double = if (list.isEmpty()) 0.0 else list.average()
/**
 * Средняя
 *
 * Центрировать заданный список list, уменьшив каждый элемент на среднее арифметическое всех элементов.
 * Если список пуст, не делать ничего. Вернуть изменённый список.
 *
 * Обратите внимание, что данная функция должна изменять содержание списка list, а не его копии.
 */
fun center(list: MutableList<Double>): MutableList<Double> {
    val temp = mean(list)
    for (i in 0 until list.size)
        list[i] = list[i] - temp
    return list
}

/**
 * Средняя
 *
 * Найти скалярное произведение двух векторов равной размерности,
 * представленные в виде списков a и b. Скалярное произведение считать по формуле:
 * C = a1b1 + a2b2 + ... + aNbN. Произведение пустых векторов считать равным 0.
 */
fun times(a: List<Int>, b: List<Int>): Int = a.zip(b) { i, j -> i * j }.sum()

/**
 * Средняя
 *
 * Рассчитать значение многочлена при заданном x:
 * p(x) = p0 + p1*x + p2*x^2 + p3*x^3 + ... + pN*x^N.
 * Коэффициенты многочлена заданы списком p: (p0, p1, p2, p3, ..., pN).
 * Значение пустого многочлена равно 0 при любом x.
 */
fun polynom(p: List<Int>, x: Int): Int {
    var acc = 0
    for (i in 0 until p.size) {
        acc += p[i] * pow(x.toDouble(), i.toDouble()).toInt()
    }
    return acc
}

/**
 * Средняя
 *
 * В заданном списке list каждый элемент, кроме первого, заменить
 * суммой данного элемента и всех предыдущих.
 * Например: 1, 2, 3, 4 -> 1, 3, 6, 10.
 * Пустой список не следует изменять. Вернуть изменённый список.
 *
 * Обратите внимание, что данная функция должна изменять содержание списка list, а не его копии.
 */
fun accumulate(list: MutableList<Int>): MutableList<Int> {
    for (i in 1 until list.size) list[i] += list[i - 1]
    return list
}

/**
 * Средняя
 *
 * Разложить заданное натуральное число n > 1 на простые множители.
 * Результат разложения вернуть в виде списка множителей, например 75 -> (3, 5, 5).
 * Множители в списке должны располагаться по возрастанию.
 */
fun factorize(n: Int): List<Int> {
    val result: MutableList<Int> = mutableListOf()
    var stopNum = n
    while (stopNum > 1) {
        val min = minDivisor(stopNum)
        result.add(min)
        stopNum /= min
    }
    return result
}

/**
 * Сложная
 *
 * Разложить заданное натуральное число n > 1 на простые множители.
 * Результат разложения вернуть в виде строки, например 75 -> 3*5*5
 * Множители в результирующей строке должны располагаться по возрастанию.
 */
fun factorizeToString(n: Int): String = factorize(n).joinToString(separator = "*")

//fun main(){
//    println(factorize(1073676289))}
/**
 * Средняя
 *
 * Перевести заданное целое число n >= 0 в систему счисления с основанием base > 1.
 * Результат перевода вернуть в виде списка цифр в base-ичной системе от старшей к младшей,
 * например: n = 100, base = 4 -> (1, 2, 1, 0) или n = 250, base = 14 -> (1, 3, 12)
 */
fun convert(n: Int, base: Int): List<Int> {
    val rez: MutableList<Int> = mutableListOf()
    var rezz = n
    if (n == 0) return listOf(0)
    while (rezz != 0) {
        rez.add(rezz % base)
        rezz /= base
    }
    return rez.reversed()
}


/**
 * Сложная
 *
 * Перевести заданное целое число n >= 0 в систему счисления с основанием 1 < base < 37.
 * Результат перевода вернуть в виде строки, цифры более 9 представлять латинскими
 * строчными буквами: 10 -> a, 11 -> b, 12 -> c и так далее.
 * Например: n = 100, base = 4 -> 1210, n = 250, base = 14 -> 13c
 */
fun convertToString(n: Int, base: Int): String = n.toString(base)

/**
 * Средняя
 *
 * Перевести число, представленное списком цифр digits от старшей к младшей,
 * из системы счисления с основанием base в десятичную.
 * Например: digits = (1, 3, 12), base = 14 -> 250
 */
fun decimal(digits: List<Int>, base: Int): Int {
    val tempList = digits.map { it.toDouble() }.reversed()
    var acc = 0.0
    for (i in 0 until tempList.size) {
        acc += tempList[i] * pow(base.toDouble(), i.toDouble()).toInt()
    }
    return acc.toInt()
}

/**
 * Сложная
 *
 * Перевести число, представленное цифровой строкой str,
 * из системы счисления с основанием base в десятичную.
 * Цифры более 9 представляются латинскими строчными буквами:
 * 10 -> a, 11 -> b, 12 -> c и так далее.
 * Например: str = "13c", base = 14 -> 250
 */
fun decimalFromString(str: String, base: Int): Int {
    val digits = mutableListOf<Int>()
    for (char in str) {
        if (char in 'a'..'z') digits.add(char - 'a' + 10)
        else digits.add(char - '0')
    }
    return decimal(digits, base)
}

/**
 * Сложная
 *
 * Перевести натуральное число n > 0 в римскую систему.
 * Римские цифры: 1 = I, 4 = IV, 5 = V, 9 = IX, 10 = X, 40 = XL, 50 = L,
 * 90 = XC, 100 = C, 400 = CD, 500 = D, 900 = CM, 1000 = M.
 * Например: 23 = XXIII, 44 = XLIV, 100 = C
 */
fun roman(n: Int): String {
    val romanNumList = mutableListOf<String>("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    val arabicNumList = mutableListOf<Int>(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    var rezString = ""
    var currentUseNum = n
    val tempList = mutableListOf<Int>()
    while (currentUseNum > 0) {
        for (i in 0..arabicNumList.size) {
            if (currentUseNum >= arabicNumList[i]) {
                currentUseNum -= arabicNumList[i]
                tempList.add(i)
                break
            }
        }
    }
    for (index in tempList) {
        rezString += romanNumList[index]
    }
    return rezString
}

//
// fun main(){
//    println(roman(3000)) }

/**
 * Очень сложная
 *
 * Записать заданное натуральное число 1..999999 прописью по-русски.
 * Например, 375 = "триста семьдесят пять",
 * 23964 = "двадцать три тысячи девятьсот шестьдесят четыре"
 */
fun russian(n: Int): String {
    var num = n
    val arrayOfNum = n.toString().map { it.toString().toInt() }
    val len = arrayOfNum.size
    val posOfThs = len - 3
    var rezStr = ""

    val rusWordsDownTen = mutableListOf<String>(
        "одна", "две", "три", "четыре", "пять",
        "шесть", "семь", "восемь", "девять"
    )
    val rusWordsUpTen = mutableListOf<String>(
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    )
    val rusWordsDown100 = mutableListOf<String>(
        "", "двадцать", "тридцать", "сорок", "пятьдесят",
        "шестьдесят", "семьдесят", "восемьдесят", "девяносто"
    )
    val rusWordsHundreds = mutableListOf<String>(
        "сто", "двести", "триста", "четыреста", "пятьсот",
        "шестьсот", "семьсот", "восемьсот", "девятьсот"
    )
    val numExceptionDownTen = mutableListOf<String>("один", "два")
    val numerationThsds = mutableListOf<String>("тысяча", "тысячи", "тысяч")
    val helpNums = arrayOf<Int>(2, 3, 4)

    var tempIndex = 0
    var indexOfThsd = 0
    var temp = posOfThs
    var tempReverse = len - posOfThs
    if (posOfThs > 0) indexOfThsd = posOfThs


    for (numI in arrayOfNum) {
        tempIndex++

        // Вывод всего что тысячного порядка
        if (tempIndex in 1..posOfThs && numI != 0) {
            if (posOfThs - 2 == arrayOfNum.indexOf(1)) {
                rezStr += when (temp) {
                    3 -> rusWordsHundreds[numI - 1] + " "
                    2 -> rusWordsUpTen[numI] + " "
                    else -> ""
                }
            } else {
                rezStr += when (temp) {
                    3 -> rusWordsHundreds[numI - 1] + " "
                    2 -> rusWordsDown100[numI - 1] + " "
                    1 -> rusWordsDownTen[numI - 1] + " "
                    else -> ""
                }
                if (tempIndex == indexOfThsd) {
                    rezStr += when {
                        helpNums.contains(numI) -> numerationThsds[1] + " "
                        1 == numI -> numerationThsds[0] + " "
                        else -> numerationThsds[2] + " "
                    }
                }
            }
        }

        temp--
        if (tempIndex in posOfThs + 1..len && numI != 0) {
            rezStr += when (tempReverse) {
                3 -> rusWordsHundreds[numI - 1]
                2 -> " " + rusWordsDown100[numI - 1]
                1 -> " " + rusWordsDownTen[numI - 1]
                else -> ""
            }
            tempReverse--
        }

    }




    return rezStr
}

fun main() {
    println(russian(100100))
}