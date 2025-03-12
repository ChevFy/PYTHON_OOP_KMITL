def is_leap(year):
   return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def day_of_year(d,m,y):
   if(d <= 0 or m <= 0 or m > 12 or y <= 0): 
      return "Invalid"
   sum = 0
   day_list = [31,29 if is_leap(y) else 28,31,30,31,30,31,31,30,31,30,31]
   if(d > day_list[m-1]): 
        return "Invalid"
   for i in range(int(m)-1):
       sum += day_list[i]
   return sum + d

try:
   d,m,y = input().split("-")
   print(f"day of year: {day_of_year(int(d),int(m),int(y))} is_leap: {is_leap(int(y))}")
except:
   print("Invalid")