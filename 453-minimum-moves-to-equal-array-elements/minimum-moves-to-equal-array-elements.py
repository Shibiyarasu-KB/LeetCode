class Solution:
    def minMoves(self, a: List[int]) -> int:
        return sum(a)-len(a)*min(a)