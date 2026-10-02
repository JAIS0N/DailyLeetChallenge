class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
            # If we have used all n opening and n closing parentheses,
            # the current combination is complete.
            result = []
            def backtrack(current: str, open_count: int, close_count: int) -> None:
                if open_count == n and close_count == n:
                    result.append(current)
                    return

            # Add an opening parenthesis if we still have one available.
                if open_count < n:
                    backtrack(current + "(", open_count + 1, close_count)

                # Add a closing parenthesis only if there is an unmatched
                # opening parenthesis available to close.
                if close_count < open_count:
                    backtrack(current + ")", open_count, close_count + 1)

                # Begin with an empty string and zero parentheses used.
            backtrack("", 0, 0)

            return result