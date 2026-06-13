import heapq

# Create an empty priority queue.
# Python's heapq implements a MIN HEAP.
pq = []

# Insert tasks with NEGATIVE priorities.
# Reason:
# heapq removes the smallest value first.
# By storing negative priorities, the task with the
# largest original priority becomes the smallest negative number.

heapq.heappush(pq, (-2, "Study"))    # Original priority = 2
heapq.heappush(pq, (-1, "Table"))    # Original priority = 1
heapq.heappush(pq, (-5, "Student"))  # Original priority = 5

# Heap contents (internal representation may vary):
# [(-5, 'Student'), (-1, 'Table'), (-2, 'Study')]
#
# Logical priority order:
# Priority 5 -> Student
# Priority 2 -> Study
# Priority 1 -> Table

# Remove the highest-priority task.
# Since this is a min heap, the smallest value (-5)
# is removed first.
priority, task = heapq.heappop(pq)

# Convert the stored negative priority
# back to its original positive value.
print(-priority, task)

# Output:
# 5 Student