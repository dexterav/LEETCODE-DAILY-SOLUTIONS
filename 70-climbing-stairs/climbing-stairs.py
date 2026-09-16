class Solution(object):
    def climbStairs(self, n):
        a = 1
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return a