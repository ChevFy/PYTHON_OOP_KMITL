def check(a):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    try:
        number = int(a)
    except ValueError:
        return "Invalid"

   
    if number <= 1 :
        return "Invalid"

    upper_limit = 10**number - 1  
    lower_limit = 10**(number - 1)  

    largest_palindrome = 0

    for i in range(upper_limit, lower_limit - 1, -1):
        if i * upper_limit < largest_palindrome:
            break  
        for j in range(i, lower_limit - 1, -1): 
            product = i * j
            if product <= largest_palindrome:
                break  
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


value = input()
print(check(value))
