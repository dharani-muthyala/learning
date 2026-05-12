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