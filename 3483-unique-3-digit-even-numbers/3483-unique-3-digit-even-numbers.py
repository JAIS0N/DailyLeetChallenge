class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
    
        # Create a frequency array for digits 0 through 9.
        available = [0] * 10

        # Count how many copies of each digit are available.
        for digit in digits:
            available[digit] += 1

        # Store the number of valid distinct three-digit even numbers.
        answer = 0

        # Check every possible three-digit even number exactly once.
        for number in range(100, 1000, 2):
            # Extract the hundreds digit.
            hundreds = number // 100

            # Extract the tens digit.
            tens = (number // 10) % 10

            # Extract the units digit.
            units = number % 10

            # Record how many copies of each digit this number requires.
            required = [0] * 10

            # Use one copy of the hundreds digit.
            required[hundreds] += 1

            # Use one copy of the tens digit.
            required[tens] += 1

            # Use one copy of the units digit.
            required[units] += 1

            # Assume the number can be formed.
            can_form = True

            # Check whether every required digit is available.
            for digit in range(10):
                # If the candidate requires too many copies, it is invalid.
                if required[digit] > available[digit]:
                    can_form = False
                    break

            # Count this candidate if all required digits are available.
            if can_form:
                answer += 1

        # Return the number of distinct valid numbers.
        return answer