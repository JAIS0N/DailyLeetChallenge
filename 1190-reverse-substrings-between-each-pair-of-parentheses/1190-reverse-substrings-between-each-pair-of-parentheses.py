class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for character in s:
            if character == "(":
                stack.append("")
            elif character == ")":
                reversed_part = stack.pop()[::-1]
                stack[-1] += reversed_part
            else:
                stack[-1] += character

        return stack[0]
        