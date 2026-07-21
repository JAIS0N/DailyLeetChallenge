class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        # Store the length of the original string.
        n = len(s)

        # Count the active sections before performing any trade.
        active_count = s.count("1")

        # Store the maximum number of zeros that can be gained.
        maximum_gain = 0

        # Store the length of the previously encountered zero run.
        previous_zero_length = None

        # Start scanning the string from the first character.
        index = 0

        # Process every maximal run in the string.
        while index < n:
            # One characters do not begin zero runs.
            if s[index] == "1":
                index += 1
                continue

            # Record where the current zero run begins.
            zero_start = index

            # Move past the entire current zero run.
            while index < n and s[index] == "0":
                index += 1

            # Calculate the length of the current zero run.
            current_zero_length = index - zero_start

            # Two consecutive zero runs have a one run between them.
            if previous_zero_length is not None:
                # Their combined length is the gain from removing that one run.
                current_gain = (
                    previous_zero_length + current_zero_length
                )

                # Keep the largest gain found so far.
                maximum_gain = max(maximum_gain, current_gain)

            # Save this zero run for pairing with the next zero run.
            previous_zero_length = current_zero_length

        # Add the best possible gain to the original number of ones.
        return active_count + maximum_gain
        