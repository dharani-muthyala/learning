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