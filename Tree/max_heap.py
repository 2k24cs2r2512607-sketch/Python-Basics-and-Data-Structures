import heapq

# Create an empty heap
heap = []

# Insert negative values
# Original values: 20, 10, 50
heapq.heappush(heap, -20)
heapq.heappush(heap, -10)
heapq.heappush(heap, -50)

# Internal heap:
# [-50, -10, -20]
#
# Since heapq is a Min Heap,
# the smallest value (-50) is at the root.

# Remove the maximum original value
largest = -heapq.heappop(heap)

print(largest)