# Find given number is Weird or not based on range
def weird_or_not(n):
    if n % 2 != 0:
        return "Weird"
    elif n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 21):
        return "Weird"
    else:
        return "Not Weird"
    
 # To check the given year is leap year or not   
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False    