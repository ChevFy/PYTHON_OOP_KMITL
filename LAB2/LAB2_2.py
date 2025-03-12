
def main(sth) :
    def date_diff(first_date, second_date):
        try:
            first = [int(x) for x in first_date.split('-')]
            second = [int(x) for x in second_date.split('-')]
        except:
            return "Invalid"

        total_first = day_of_years("{0} {1} {2}".format(first[0], first[1], first[2]))
        total_second = day_of_years("{0} {1} {2}".format(second[0], second[1], second[2]))

        if (second[1] < first[1]):
            total = day_in_year(first[2]) - abs(total_second - total_first) + 1
            for i in range(first[2], second[2] - 1):
                total += day_in_year(i)
        elif (second[2] == first[2]):
            return abs(total_second - total_first) + 1
        else:
            total = abs(total_second - total_first) + 1
            for i in range(first[2], second[2]):
                total += day_in_year(i)
        return total

    def day_in_year(year):
        return 366 if is_leap(year) else 365

    def day_of_years(a):
        try:
            day, month, year = map(int, a.split())
        except :
            return "Invalid"

        m = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (0 <= year <= 2024 and 1 <= month <= 12 and 1 <= day <= m[month - 1]):
            return "Invalid"

        sum = 0
        for i in range(month - 1):
            sum += m[i]
        return sum + day

    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    try:
        date1, date2 = values.split(',')
        return date_diff(date1, date2)
    except :
       return "Invalid"

values = input()
print(main(values))
