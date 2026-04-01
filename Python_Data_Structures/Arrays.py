# To return reverse of an array
def reverseArray(a):
    return a[::-1]

# 2D array
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglassSum(arr):
    # Write your code here
    max_sum = -9 * 7   

    for i in range(4):            
        for j in range(4):        
            
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hourglass = top + mid + bottom
            if hourglass > max_sum:
                max_sum = hourglass

    return max_sum

# Dynamic array
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    lastAnswer = 0
    result = []

    for q in queries:
        t, x, y = q

        idx = (x ^ lastAnswer) % n

        if t == 1:
            arr[idx].append(y)

        elif t == 2:
            value = arr[idx][y % len(arr[idx])]
            lastAnswer = value
            result.append(lastAnswer)

    return result   

# Left Rotation
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def rotateLeft(d, arr):
    # Write your code here
    d = d % len(arr)      
    return arr[d:] + arr[:d]

# Sparse Arrays
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#
def matchingStrings(stringList, queries):
    # Write your code here
    freq = {}
    
    for s in stringList:
        freq[s] = freq.get(s, 0) + 1

    result = []
    
    for q in queries:
        result.append(freq.get(q, 0))

    return result

# Array Manipulation
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def arrayManipulation(n, queries):
    arr = [0] * (n + 2)  
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
    max_val = 0
    current = 0
    for i in range(1, n + 1):
        current += arr[i]
        if current > max_val:
            max_val = current
    return max_val

