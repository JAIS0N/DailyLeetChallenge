class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        moves=moves.lower()
        for move in moves:
            if move == "u":
                y=y+1
            if move == "d":
                y=y-1
            if move == "l":
                x=x-1
            if move == "r":
                x=x+1
        if x==0 and y == 0:
            return True
        else: 
            return False
