class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = set()
        upper = set()
        invalid = set()

        for ch in word:
            if ch.islower():
                # lowercase appearing after uppercase -> invalid
                if ch in upper:
                    invalid.add(ch)

                lower.add(ch)

            else:
                ch_lower = ch.lower()
                upper.add(ch_lower)

        return len((lower & upper) - invalid)