class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, path, used):
            if len(nums) == len(path):
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(start, path, used)
                path.pop()
                used[i] = False

        used = [False] * len(nums)
        backtrack(0, [], used)
        return result