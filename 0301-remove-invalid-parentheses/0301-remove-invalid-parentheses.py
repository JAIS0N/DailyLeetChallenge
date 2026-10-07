class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        # Count how many opening and closing parentheses must be removed.
        left_remove = 0
        right_remove = 0

        # Scan the string to determine the minimum required removals.
        for char in s:
            if char == '(':
                # This opening parenthesis is currently unmatched.
                left_remove += 1

            elif char == ')':
                if left_remove > 0:
                    # Match this closing parenthesis with a previous opening one.
                    left_remove -= 1
                else:
                    # There is no opening parenthesis available for this one.
                    right_remove += 1

        # A set prevents duplicate valid strings.
        result = set()

        def backtrack(
            index: int,
            left_remove: int,
            right_remove: int,
            balance: int,
            current: list[str]
        ) -> None:

            # If we processed the whole string, check whether it is valid.
            if index == len(s):
                if left_remove == 0 and right_remove == 0 and balance == 0:
                    result.add(''.join(current))
                return

            # Current character being processed.
            char = s[index]

            # If this is an opening parenthesis, we may remove it.
            if char == '(' and left_remove > 0:
                backtrack(
                    index + 1,
                    left_remove - 1,
                    right_remove,
                    balance,
                    current
                )

            # If this is a closing parenthesis, we may remove it.
            elif char == ')' and right_remove > 0:
                backtrack(
                    index + 1,
                    left_remove,
                    right_remove - 1,
                    balance,
                    current
                )

            # Letters must always be kept.
            if char != '(' and char != ')':
                current.append(char)

                backtrack(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance,
                    current
                )

                current.pop()

            # Keep an opening parenthesis.
            elif char == '(':
                current.append(char)

                backtrack(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance + 1,
                    current
                )

                current.pop()

            # Keep a closing parenthesis only when it has an opening match.
            elif balance > 0:
                current.append(char)

                backtrack(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance - 1,
                    current
                )

                current.pop()

        # Start the search.
        backtrack(
            0,
            left_remove,
            right_remove,
            0,
            []
        )

        return list(result)
        