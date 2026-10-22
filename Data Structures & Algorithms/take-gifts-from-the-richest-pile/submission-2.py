import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-pile for pile in gifts]
        heapq.heapify(maxHeap)

        while k:
            heapq.heappush(maxHeap, -int(sqrt(-heapq.heappop(maxHeap))))
            k -= 1

        return -sum(maxHeap)