@file:Suppress("UNUSED_PARAMETER", "ConvertCallChainIntoSequence")

package lesson6.task1

import java.lang.NumberFormatException
import java.util.Collections.max

/**
 * Пример
 *
 * Время представлено строкой вида "11:34:45", содержащей часы, минуты и секунды, разделённые двоеточием.
 * Разобрать эту строку и рассчитать количество секунд, прошедшее с начала дня.
 */
fun timeStrToSeconds(str: String): Int {
    val parts = str.split(":")
    var result = 0
    for (part in parts) {
        val number = part.toInt()
        result = result * 60 + number
    }
    return result
}

/**
 * Пример
 *
 * Дано число n от 0 до 99.
 * Вернуть его же в виде двухсимвольной строки, от "00" до "99"
 */
fun twoDigitStr(n: Int) = if (n in 0..9) "0$n" else "$n"

/**
 * Пример
 *
 * Дано seconds -- время в секундах, прошедшее с начала дня.
 * Вернуть текущее время в виде строки в формате "ЧЧ:ММ:СС".
 */
fun timeSecondsToStr(seconds: Int): String {
    val hour = seconds / 3600
    val minute = (seconds % 3600) / 60
    val second = seconds % 60
    return String.format("%02d:%02d:%02d", hour, minute, second)
}

/**
 * Пример: консольный ввод
 */
//fun main() {
//    println("Введите время в формате ЧЧ:ММ:СС")
//    val line = readLine()
//   if (line != null) {
//       val seconds = timeStrToSeconds(line)
//       if (seconds == -1) {
//           println("Введённая строка $line не соответствует формату ЧЧ:ММ:СС")
//       } else {
//           println("Прошло секунд с начала суток: $seconds")
//       }
//   } else {
//        println("Достигнут <конец файла> в процессе чтения строки. Программа прервана")
//    }
//}


/**
 * Средняя
 *
 * Дата представлена строкой вида "15 июля 2016".
 * Перевести её в цифровой формат "15.07.2016".
 * День и месяц всегда представлять двумя цифрами, например: 03.04.2011.
 * При неверном формате входной строки вернуть пустую строку.
 *
 * Обратите внимание: некорректная с точки зрения календаря дата (например, 30.02.2009) считается неверными
 * входными данными.
 */
val dataList = mapOf(
    "января" to Pair("1", 31),
    "февраля" to Pair("2", 28),
    "марта" to Pair("3", 31),
    "апреля" to Pair("4", 30),
    "мая" to Pair("5", 31),
    "июня" to Pair("6", 30),
    "июля" to Pair("7", 31),
    "августа" to Pair("8", 31),
    "сентября" to Pair("9", 30),
    "октября" to Pair("10", 31),
    "ноября" to Pair("11", 30),
    "декабря" to Pair("12", 31)
)

fun leapYear(year: Int): Boolean = year % 4 == 0 || (year % 100 == 0 && year % 400 != 0)

fun dateStrToDigit(str: String): String {
    val workLine = str.split(" ")
    var rezString = ""

    if (workLine.size != 3) return ""
    if (!dataList.containsKey(workLine[1])) return ""

    val month = (dataList[workLine[1]]?.first)?.toInt() ?: 0
    val day: Int
    val year: Int

    try {
        day = workLine[0].toInt()
        year = workLine[2].toInt()
    } catch (e: NumberFormatException) {
        return ""
    }

    if (year < 0) return ""

    if (leapYear(year) && month == 2 && day <= 29) {
        rezString += when {
            day < 10 -> "0$day.02.$year"
            else -> "$day.02.$year"
        }
    } else {
        if (day < dataList[workLine[1]]?.second ?: 0) {
            rezString += when {
                day < 10 -> "0$day."
                else -> "$day."
            }
        } else return ""
        rezString += if (month < 10) "0$month.$year"
        else "$month.$year"
    }
    return rezString
}

//fun main() {
//    println(dateDigitToStr("31.01.1"))
//}

/**
 * Средняя
 *
 * Дата представлена строкой вида "15.07.2016".
 * Перевести её в строковый формат вида "15 июля 2016".
 * При неверном формате входной строки вернуть пустую строку
 *
 * Обратите внимание: некорректная с точки зрения календаря дата (например, 30 февраля 2009) считается неверными
 * входными данными.
 */
val digitalDataList = dataList.map { it.value.first.toInt() to Pair(it.key, it.value.second) }.toMap()

fun dateDigitToStr(digital: String): String {
    val workLine = digital.split(".")
    var rezString = ""
    val day: Int
    val year: Int
    val monthRe: Int

    try {
        monthRe = workLine[1].toInt()
        day = workLine[0].toInt()
        year = workLine[2].toInt()
    } catch (e: NumberFormatException) {
        return ""
    }
    if (day < 10) {
        println(day)
    }

    val month = digitalDataList[workLine[1].toInt()]?.first

    if (year < 0) return ""
    if (workLine.size != 3) return ""
    if (!digitalDataList.containsKey(workLine[1].toInt())) return ""

    if (leapYear(year) && month == "февраля" && day <= 29) {
        rezString += when {
            day < 10 -> "$day $month $year"
            else -> "$day $month $year"
        }
    } else {
        if (day < digitalDataList[workLine[1].toInt()]?.second ?: 0) {
            rezString += "$day "
        } else return ""
        rezString += "$month $year"
    }
    return rezString
}

/**
 * Средняя
 *
 * Номер телефона задан строкой вида "+7 (921) 123-45-67".
 * Префикс (+7) может отсутствовать, код города (в скобках) также может отсутствовать.
 * Может присутствовать неограниченное количество пробелов и чёрточек,
 * например, номер 12 --  34- 5 -- 67 -89 тоже следует считать легальным.
 * Перевести номер в формат без скобок, пробелов и чёрточек (но с +), например,
 * "+79211234567" или "123456789" для приведённых примеров.
 * Все символы в номере, кроме цифр, пробелов и +-(), считать недопустимыми.
 * При неверном формате вернуть пустую строку.
 *
 * PS: Дополнительные примеры работы функции можно посмотреть в соответствующих тестах.
 */
fun flattenPhoneNumber(phone: String): String {
    val phoneClear = phone.replace("[ ()-]".toRegex(), "")
    if (!phoneClear.matches("^[+\\d]\\d*$".toRegex())) return ""
    return phoneClear
}

/**
 * Средняя
 *
 * Результаты спортсмена на соревнованиях в прыжках в длину представлены строкой вида
 * "706 - % 717 % 703".
 * В строке могут присутствовать числа, черточки - и знаки процента %, разделённые пробелами;
 * число соответствует удачному прыжку, - пропущенной попытке, % заступу.
 * Прочитать строку и вернуть максимальное присутствующее в ней число (717 в примере).
 * При нарушении формата входной строки или при отсутствии в ней чисел, вернуть -1.
 */
fun bestLongJump(jumps: String): Int {
    //val jumpsClear = jumps.replace("[-%]".toRegex(), "")
    //if (!jumpsClear.matches("^[+\\d]\\d*".toRegex())) return -1
    //println(jumpsClear.split(" "))
    //val jumpsClear = Regex("[-%]").split(jumps)
    //val jumpsClear = jumps.replace("[-%]".toRegex(), "")
    //val jumpsClearRez = jumpsClear.split(" ").toMutableList()
    //println(jumpsClear)
    //println(max(jumpsClear.map { it.toInt() }))
    //return try {
    //    max(jumpsClear.map { it.toInt() })
    //} catch (e: NumberFormatException) {
    //    -1
    //}
    val jumpList = jumps.split(" ")
    var bestJump = -1
    for (jump in jumpList) {
        try {
            val tempJump = jump.toInt()
            if (tempJump > bestJump) bestJump = tempJump
        } catch (e: NumberFormatException) {
            if (!(jump == "-" || jump == "%")) return -1
        }
    }
    return bestJump
}


/**
 * Сложная
 *
 * Результаты спортсмена на соревнованиях в прыжках в высоту представлены строкой вида
 * "220 + 224 %+ 228 %- 230 + 232 %%- 234 %".
 * Здесь + соответствует удачной попытке, % неудачной, - пропущенной.
 * Высота и соответствующие ей попытки разделяются пробелом.
 * Прочитать строку и вернуть максимальную взятую высоту (230 в примере).
 * При нарушении формата входной строки, а также в случае отсутствия удачных попыток,
 * вернуть -1.
 */
fun bestHighJump(jumps: String): Int {
    val jumpList = jumps.split(" ")
    var bestJump = -1
    for ((index, jump) in jumpList.withIndex()) {
        try {
            val tempJump = jump.toInt()
            if ((index < jumpList.size - 1) && jumpList[index + 1].contains("+")) {
                if (tempJump > bestJump) bestJump = tempJump
            }
        } catch (e: NumberFormatException) {
            for (symbol in jump) {
                if (!setOf('-', '%', '+').contains(symbol)) return -1
            }
        }
    }
    return bestJump
}

/**
 * Сложная
 *
 * В строке представлено выражение вида "2 + 31 - 40 + 13",
 * использующее целые положительные числа, плюсы и минусы, разделённые пробелами.
 * Наличие двух знаков подряд "13 + + 10" или двух чисел подряд "1 2" не допускается.
 * Вернуть значение выражения (6 для примера).
 * Про нарушении формата входной строки бросить исключение IllegalArgumentException
 */
fun isItNumber(number: String): Boolean {
    if (Regex("""[^0123456789]""").find(number) != null) return false
    return true
}

fun isItSymbol(symbol: String): Boolean {
    if (symbol == "+" || symbol == "-") return true
    return false
}

fun plusMinus(expression: String): Int {
    val tempExpression = expression.split(" ")
    var tempNum = 0
    var rezNum = 0
    var tempSymb = "+"
    var tempEx = "+"
    loop@ for (elem in tempExpression) {
        if (isItSymbol(elem) && isItSymbol(tempEx)) throw IllegalArgumentException()
        tempEx = elem

        when {
            isItNumber(elem) -> tempNum = elem.toInt()
            isItSymbol(elem) -> {
                tempSymb = elem
                continue@loop
            }
            else -> throw IllegalArgumentException()
        }
        when (tempSymb) {
            "+" -> rezNum += tempNum
            "-" -> rezNum -= tempNum
            else -> throw IllegalArgumentException()
        }
    }
    return rezNum
}

/**
 * Сложная
 *
 * Строка состоит из набора слов, отделённых друг от друга одним пробелом.
 * Определить, имеются ли в строке повторяющиеся слова, идущие друг за другом.
 * Слова, отличающиеся только регистром, считать совпадающими.
 * Вернуть индекс начала первого повторяющегося слова, или -1, если повторов нет.
 * Пример: "Он пошёл в в школу" => результат 9 (индекс первого 'в')
 */
fun firstDuplicateIndex(str: String): Int {
    val listStr = str.trim().split(" ")
    var tempWord = ""
    var idx = 0
    println(listStr)

    for (elem in listStr) {
        if (elem.toLowerCase() != tempWord) {
            tempWord = elem.toLowerCase()
        } else {
            return idx - elem.length - 1
        }
        idx += elem.length + 1
    }
    return -1
}


/**
 * Сложная
 *
 * Строка содержит названия товаров и цены на них в формате вида
 * "Хлеб 39.9; Молоко 62; Курица 184.0; Конфеты 89.9".
 * То есть, название товара отделено от цены пробелом,
 * а цена отделена от названия следующего товара точкой с запятой и пробелом.
 * Вернуть название самого дорогого товара в списке (в примере это Курица),
 * или пустую строку при нарушении формата строки.
 * Все цены должны быть больше либо равны нуля.
 */
fun mostExpensive(description: String): String? {
    if (description == "") return ""

    val proviantSplit = description.split("; ")
    val productsToPrices = mutableMapOf<Double, String>()

    for (elem in proviantSplit) {
        val temp = elem.split(" ")
        try {
            productsToPrices[temp[1].toDouble()] = temp[0]
        } catch (Exception: NumberFormatException) {
            return ""
        }
    }
    return productsToPrices[max(productsToPrices.keys)]
}


/**
 * Сложная
 *
 * Перевести число roman, заданное в римской системе счисления,
 * в десятичную систему и вернуть как результат.
 * Римские цифры: 1 = I, 4 = IV, 5 = V, 9 = IX, 10 = X, 40 = XL, 50 = L,
 * 90 = XC, 100 = C, 400 = CD, 500 = D, 900 = CM, 1000 = M.
 * Например: XXIII = 23, XLIV = 44, C = 100
 *
 * Вернуть -1, если roman не является корректным римским числом
 */
fun fromRoman(roman: String): Int = TODO()

/**
 * Очень сложная
 *
 * Имеется специальное устройство, представляющее собой
 * конвейер из cells ячеек (нумеруются от 0 до cells - 1 слева направо) и датчик, двигающийся над этим конвейером.
 * Строка commands содержит последовательность команд, выполняемых данным устройством, например +>+>+>+>+
 * Каждая команда кодируется одним специальным символом:
 *	> - сдвиг датчика вправо на 1 ячейку;
 *  < - сдвиг датчика влево на 1 ячейку;
 *	+ - увеличение значения в ячейке под датчиком на 1 ед.;
 *	- - уменьшение значения в ячейке под датчиком на 1 ед.;
 *	[ - если значение под датчиком равно 0, в качестве следующей команды следует воспринимать
 *  	не следующую по порядку, а идущую за соответствующей следующей командой ']' (с учётом вложенности);
 *	] - если значение под датчиком не равно 0, в качестве следующей команды следует воспринимать
 *  	не следующую по порядку, а идущую за соответствующей предыдущей командой '[' (с учётом вложенности);
 *      (комбинация [] имитирует цикл)
 *  пробел - пустая команда
 *
 * Изначально все ячейки заполнены значением 0 и датчик стоит на ячейке с номером N/2 (округлять вниз)
 *
 * После выполнения limit команд или всех команд из commands следует прекратить выполнение последовательности команд.
 * Учитываются все команды, в том числе несостоявшиеся переходы ("[" при значении под датчиком не равном 0 и "]" при
 * значении под датчиком равном 0) и пробелы.
 *
 * Вернуть список размера cells, содержащий элементы ячеек устройства после завершения выполнения последовательности.
 * Например, для 10 ячеек и командной строки +>+>+>+>+ результат должен быть 0,0,0,0,0,1,1,1,1,1
 *
 * Все прочие символы следует считать ошибочными и формировать исключение IllegalArgumentException.
 * То же исключение формируется, если у символов [ ] не оказывается пары.
 * Выход за границу конвейера также следует считать ошибкой и формировать исключение IllegalStateException.
 * Считать, что ошибочные символы и непарные скобки являются более приоритетной ошибкой чем выход за границу ленты,
 * то есть если в программе присутствует некорректный символ или непарная скобка, то должно быть выброшено
 * IllegalArgumentException.
 * IllegalArgumentException должен бросаться даже если ошибочная команда не была достигнута в ходе выполнения.
 *
 */
fun computeDeviceCells(cells: Int, commands: String, limit: Int): List<Int> = TODO()
