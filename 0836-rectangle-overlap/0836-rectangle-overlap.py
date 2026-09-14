class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # The rectangles overlap horizontally if the first rectangle starts
        # before the second rectangle ends and the second starts before the first ends.
        horizontal_overlap = rec1[0] < rec2[2] and rec2[0] < rec1[2]

        # The rectangles overlap vertically if the first rectangle starts
        # below the second rectangle's top and the second starts below the first's top.
        vertical_overlap = rec1[1] < rec2[3] and rec2[1] < rec1[3]

        # Positive width and positive height produce a positive intersection area.
        return horizontal_overlap and vertical_overlap
        