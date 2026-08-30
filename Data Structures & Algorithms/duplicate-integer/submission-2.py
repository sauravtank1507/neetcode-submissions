class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        i = j = 0
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = 2
                return True
        return False