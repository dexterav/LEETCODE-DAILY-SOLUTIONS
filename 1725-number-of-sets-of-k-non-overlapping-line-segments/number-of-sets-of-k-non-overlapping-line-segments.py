class Solution(object):
    def numberOfSets(self, n, k):
        a = n + k - 1
        b = 2 * k

        answer = 1

        for i in range(1, b + 1):
            answer = answer * (a - i + 1) // i

        return answer % (10**9 + 7)