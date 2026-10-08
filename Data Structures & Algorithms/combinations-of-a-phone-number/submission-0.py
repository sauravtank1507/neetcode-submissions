class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap  = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
                    "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []

        def backtrack(start, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for char in hashMap[digits[start]]:
                backtrack(start + 1, path + char)

        if digits:
            backtrack(0, "")
        return result