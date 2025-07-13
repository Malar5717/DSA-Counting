"""
Problem: Majority Element
Leetcode: https://leetcode.com/problems/majority-element/
Topic: DSA Counting / Frequency / Boyer-Moore Voting Algorithm
Status: ✅ Passed
Approach:
- Used Boyer-Moore Voting Algorithm
- Iterates once, adjusts vote count based on majority presence

Learnings:
- Clever use of votes lets you track the majority without extra space
- Works only if majority element is guaranteed (> n/2)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate, votes = None, 0
        for num in nums:
            if votes == 0:
                candidate = num
            votes += 1 if num == candidate else -1
        return candidate
