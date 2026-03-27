# To print square roots upto given range
def squares_upto(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# To concat the given numbers to string
def concat_numbers(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result