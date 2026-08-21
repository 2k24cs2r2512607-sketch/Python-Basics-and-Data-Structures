import heapq
pq=[]
heapq.heappush(pq,(2,"Study"))
heapq.heappush(pq,(1,"Table"))
heapq.heappush(pq,(-1,"Student"))
heapq.heappush(pq,(-3,"Student"))
print(heapq.heappop(pq))