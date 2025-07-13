"""
Problem: Q1497 Check if Array Pairs Are Divisible by K
Leetcode: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

Approach: My original idea using sorting, used[], and multiples set.
Status: TLE on large input (k=51054)
Learning: abs() doesn't work well for divisibility, and large set() is slow.
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr.sort()
        n = len(arr)
        used = [False] * n

        for i in range(n):
            if used[i]:
                continue

            found = False
            for j in range(n - 1, i, -1):
                if not used[j] and (arr[i] + arr[j]) % k == 0:
                    used[i] = True
                    used[j] = True
                    found = True
                    break

            if not found:
                return False

        return True
