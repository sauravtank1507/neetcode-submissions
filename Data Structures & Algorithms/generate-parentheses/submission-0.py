class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backtrack(open_, close_):
            if open_ == close_ == n:
                result.append("".join(stack))
                return

            if open_ < n:
                stack.append("(")
                backtrack(open_ + 1, close_)
                stack.pop()

            if close_ < open_:
                stack.append(")")
                backtrack(open_, close_ + 1)
                stack.pop()

        backtrack(0, 0)
        return result