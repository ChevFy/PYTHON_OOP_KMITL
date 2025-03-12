def wow(num):
    try :
        a = int(num)
    except ValueError :
        return "Invalid"

    if a >= 10 or a < 0 :
        return "Invalid"
    else :
       return (int('{0}'.format(a)) + int('{0}{0}'.format(a)) + int('{0}{0}{0}'.format(a)) + int('{0}{0}{0}{0}'.format(a)))


value = input()
print(wow(value))