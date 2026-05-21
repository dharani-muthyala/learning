# Maximum Element
def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:

        query = op.split()

        # Push operation
        if query[0] == '1':

            val = int(query[1])
            stack.append(val)

            if not max_stack or val >= max_stack[-1]:
                max_stack.append(val)

        # Pop operation
        elif query[0] == '2':

            removed = stack.pop()

            if removed == max_stack[-1]:
                max_stack.pop()

        # Print maximum
        elif query[0] == '3':

            result.append(max_stack[-1])

    return result

# Balanced Brackets
def isBalanced(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        # Opening brackets
        if ch in "({[":
            stack.append(ch)

        # Closing brackets
        else:

            if not stack or stack[-1] != pairs[ch]:
                return "NO"

            stack.pop()

    return "YES" if not stack else "NO"

# Equal Stacks
def equalStacks(h1, h2, h3):

    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    i = j = k = 0

    while True:

        # If any stack becomes empty
        if i == len(h1) or j == len(h2) or k == len(h3):
            return 0

        # Equal height found
        if sum1 == sum2 == sum3:
            return sum1

        # Remove from tallest stack
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[i]
            i += 1

        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[j]
            j += 1

        else:
            sum3 -= h3[k]
            k += 1

# Game of Two Stacks
def twoStacks(x, a, b):

    total = 0
    count = 0
    i = 0
    j = 0

    # Take elements from stack a first
    while i < len(a) and total + a[i] <= x:
        total += a[i]
        i += 1

    count = i

    # Try adding elements from b
    while j < len(b):

        total += b[j]
        j += 1

        # Remove from a if total exceeds x
        while total > x and i > 0:
            i -= 1
            total -= a[i]

        # If still valid, update answer
        if total <= x:
            count = max(count, i + j)

    return count            