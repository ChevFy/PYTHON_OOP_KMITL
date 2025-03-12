def value(a):
    try:
        
        lst = eval(a)
        if not isinstance(lst, (list)):
            return "Invalid"
        
       
        if not all(isinstance(x, int) for x in lst):
            return "Invalid"

    except (ValueError, SyntaxError, NameError):
        return "Invalid"

    
    l = len(lst)
    if l <= 1:
        return "Invalid"

   
    max = -10000000
    count = 0
    for i in range(l):
        for j in range(i + 1, l):  
            temp = lst[i] * lst[j]
            if temp > max:
                max = temp
                count = 1  
            elif temp == max:
                count += 1 

   
    if count > 1:
        return "Invalid"

    return max


data = input()
print(value(data))
