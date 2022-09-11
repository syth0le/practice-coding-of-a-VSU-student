def check_data(data):
    day, month, year = data
    long_months = [1, 3, 5, 7, 8, 10, 12]

    def check_is_high_year(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    def is_valid_day(day, month, is_high_year):
        if day not in range(1, 32):
            return False
        if month == 2:
            if is_high_year and day not in range(1, 30):
                return False
            if not is_high_year and day not in range(1, 29):
                return False
        if month not in long_months and day == 31:
            return False
        return True

    is_high_year = check_is_high_year(year)

    def is_valid_year(year):
        return year in range(1950, 2301)

    if not is_valid_year(year):
        return False

    if not is_valid_day(day, month, is_high_year):
        return False

    return True


N = int(input())
results = []
for i in range(N):
    temp = list(map(int, input().split()))
    answer = 'YES' if check_data(temp) else 'NO'
    results.append(answer)

for i in results:
    print(i)
