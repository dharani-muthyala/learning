# Minimum average waiting time
import heapq

def minimumAverage(customers):

    # Sort by arrival time
    customers.sort()

    n = len(customers)

    heap = []
    time = 0
    i = 0
    total_wait = 0

    while i < n or heap:

        # If no customer is available, move time
        if not heap and time < customers[i][0]:
            time = customers[i][0]

        # Add all customers who have arrived
        while i < n and customers[i][0] <= time:
            arrival, cook = customers[i]
            heapq.heappush(heap, (cook, arrival))
            i += 1

        # Process shortest job
        cook, arrival = heapq.heappop(heap)

        time += cook

        total_wait += (time - arrival)

    return total_wait // n

# QHEAP1

heap = []
removed = {}

Q = int(input())

for _ in range(Q):

    query = list(map(int, input().split()))

    # Insert
    if query[0] == 1:

        heapq.heappush(heap, query[1])

    # Delete
    elif query[0] == 2:

        val = query[1]
        removed[val] = removed.get(val, 0) + 1

    # Print minimum
    else:

        # Remove deleted elements from top
        while heap and removed.get(heap[0], 0):

            removed[heap[0]] -= 1

            if removed[heap[0]] == 0:
                del removed[heap[0]]

            heapq.heappop(heap)

        print(heap[0])

# Jesse and Cookies

def cookies(k, A):

    heapq.heapify(A)

    operations = 0

    while len(A) > 1 and A[0] < k:

        first = heapq.heappop(A)
        second = heapq.heappop(A)

        new_cookie = first + (2 * second)

        heapq.heappush(A, new_cookie)

        operations += 1

    return operations if A[0] >= k else -1

# Find the Running Median

def runningMedian(a):

    lower = []   # max heap (store negative values)
    upper = []   # min heap

    result = []

    for num in a:

        # Insert into heaps
        if not lower or num <= -lower[0]:
            heapq.heappush(lower, -num)
        else:
            heapq.heappush(upper, num)

        # Balance heaps
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))

        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))

        # Calculate median
        if len(lower) == len(upper):
            median = (-lower[0] + upper[0]) / 2

        else:
            median = float(-lower[0])

        result.append(median)

    return result