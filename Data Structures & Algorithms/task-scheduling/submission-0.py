class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() 

        while maxHeap or queue:   #if any one is non-empty then there is an empty task
            time += 1
            if maxHeap:
                x = heapq.heappop(maxHeap) + 1
                if x:
                    queue.append([x, n + time])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time