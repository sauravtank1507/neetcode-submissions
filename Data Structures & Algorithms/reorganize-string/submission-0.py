class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        maxHeap = [[-count, char] for char, count in cnt.items()]

        heapq.heapify(maxHeap)

        res = ""
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res