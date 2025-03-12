def lab(data):
    def ceil(number):
        if int(number) == 0:
            return 1
        else:
            if number % int(number) != 0:
                return int(number) + 1
            else:
                return int(number)

    if len(data) != 4:
        return "Invalid"

    try:
        start_hour, start_minute, end_hour, end_minute = map(int, data)
    except ValueError:
        return "Invalid"


    if (
        start_hour < 0 or end_hour < 0 or start_minute < 0 or end_minute < 0
        or start_minute > 59 or end_minute > 59 or start_hour > 23 or end_hour > 23
        or start_hour < 7 or end_hour < 7
    ):
        return "Invalid"

    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute
    result = end_time - start_time

    if result <= 15 and result >= 0:
        return 0
    elif result > 15 and result <= 180:
        return ceil(result / 60) * 10
    elif result > 180 and result <= 360:
        return 30 + (ceil(result / 60) - 3) * 20
    elif result > 360:
        return 200
    else:
        return "Invalid"

value = input().split()

print(lab(value))


