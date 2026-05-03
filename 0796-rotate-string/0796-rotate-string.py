class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Condition 1: lengths must match
        if len(s) != len(goal):
            return False

        # Condition 2: goal must exist in doubled string
        doubled = s + s          # contains ALL rotations
        return goal in doubled   # check if goal is one of them
        