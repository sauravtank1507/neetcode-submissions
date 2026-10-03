class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, used):
            if len(nums) == len(path):
                result.append(path[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i and  nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True

                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        nums.sort()

        used = [False] * len(nums)
        backtrack([], used)
        return result