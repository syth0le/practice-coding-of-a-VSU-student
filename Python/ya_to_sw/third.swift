var i = readLine()
func calc(_ input: String?) -> String {
    var result = ""
    guard let input = input else {
        return result
    }
    var builds = input.split(separator: " ").map{ Int($0)}.compactMap{$0}

    guard let maxNum = builds.max(), let maxIndex = builds.firstIndex(of: maxNum) else { return result }
    if 5 - maxNum > 0 {
        builds = builds.map{$0 + 5 -  maxNum}
    }

    for index in 0..<builds.count {
        let nextIndex = index + 1 < builds.count ? index + 1 : index
        if nextIndex <  maxIndex {
            if builds[nextIndex] < builds[index]  {
                builds[nextIndex] = builds[index]
            }
            if builds[nextIndex] > builds [index] {
                let diff =  builds[nextIndex] - builds[index]
                builds[index] = builds[nextIndex] - diff
            }
        } else {
            if index + 2 < builds.count {
                let a = builds[index]
                let b = builds[nextIndex]
                let c = builds[nextIndex + 1]

                if a > b && b < c {
                    let diffA = a - b
                    let diffC = c - b
                    if diffA > diffC {
                        builds[nextIndex] += diffC
                    } else {
                        builds[nextIndex] += diffA
                    }
                }
            }

        }

    }

    builds.forEach {
        if $0 <= 5 {
            result += "\($0) "
        } else {
            result += "5 "
        }
    }

    return String(result.dropLast())
}

print(calc(i))