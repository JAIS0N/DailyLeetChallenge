

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Count how many occurrences of each character remain unprocessed.
        remaining_count = Counter(s)

        # Use a list as a stack to construct the answer.
        stack = []

        # Track which characters are currently present in the stack.
        characters_in_stack = set()

        # Process each character from left to right.
        for current_character in s:
            # The current occurrence is now being processed,
            # so decrease its remaining count.
            remaining_count[current_character] -= 1

            # If the character is already included in the stack,
            # I should not add it again because every distinct
            # character must appear exactly once.
            if current_character in characters_in_stack:
                continue

            # Remove characters from the end of the stack when:
            # 1. The top character is greater than the current character,
            #    meaning removing it would make the result smaller.
            # 2. The top character appears again later,
            #    meaning it can safely be added back in the future.
            while (
                stack
                and stack[-1] > current_character
                and remaining_count[stack[-1]] > 0
            ):
                # Remove the larger character from the stack.
                removed_character = stack.pop()

                # Mark the removed character as no longer being in the stack.
                characters_in_stack.remove(removed_character)

            # Add the current character to the stack.
            stack.append(current_character)

            # Mark the current character as included.
            characters_in_stack.add(current_character)

        # Convert the stack into the final answer string.
        return "".join(stack)