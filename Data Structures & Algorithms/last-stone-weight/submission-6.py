import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            sec_heaviest = heapq.heappop(stones)

            if sec_heaviest > heaviest:
                heapq.heappush(stones, heaviest - sec_heaviest)

        stones.append(0)
        return abs(stones[0])