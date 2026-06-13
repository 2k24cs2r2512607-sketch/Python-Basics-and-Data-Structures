import heapq

# Create an empty heap.
# Python's heapq module implements a MIN HEAP.
heap = []

# Insert elements into the heap.
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

# Current heap:
# [5, 10, 20, 30]
#
# Logical tree representation:
#
#         5
#       /   \
#     10     20
#    /
#   30
#
# Min Heap Property:
# Parent node <= Child nodes

print("Heap:", heap)

# Access the minimum element.
# In a Min Heap, the root (index 0) always contains the smallest value.
print("Minimum Element:", heap[0])

# Remove and return the minimum element.
removed = heapq.heappop(heap)

# Steps performed internally:
# 1. Remove root (5)
# 2. Move last element (30) to root
# 3. Restore heap property using heapify/sift-down
#
# Resulting heap:
#
#         10
#       /    \
#     30      20

print("Removed Element:", removed)
print("Heap After Pop:", heap)