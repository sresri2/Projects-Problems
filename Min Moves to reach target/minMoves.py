class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        while target != 1:
            if maxDoubles >0 and target %2==0:
                target=int(target/2)
                moves += 1
                maxDoubles-=1
            else:
                if maxDoubles==0:
                    return moves + (target-1)
                else:
                    target -=1
                    moves += 1
        return int(moves)

print(Solution().minMoves(12,4))