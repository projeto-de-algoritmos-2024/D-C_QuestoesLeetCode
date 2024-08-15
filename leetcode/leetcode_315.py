"""
Problem: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Difficulty: hard
Solved: True
"""

from typing import List


class Solution:

    def merge(
        self, left: list[tuple[int, int, int]], right: list[tuple[int, int, int]]
    ) -> list[tuple[int, int, int]]:
        i = 0
        j = 0
        result = []
        for item in left:
            while j < len(right) and item[0] > right[j][0]:
                j += 1
            item[2] += j

        j = 0
        while i < len(left) and j < len(right):
            a = left[i]
            b = right[j]

            if a[0] <= b[0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i < len(left):
            result += left[i:]

        if j < len(right):
            result += right[j:]

        return result

    def find_smaller(self, arr: list[tuple[int, int, int]]):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return self.merge(self.find_smaller(left), self.find_smaller(right))

    def countSmaller(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        to_count = []
        for idx, item in enumerate(nums):
            to_count.append([item, idx, 0])

        result = self.find_smaller(to_count)
        for idx, item in enumerate(result):
            output[item[1]] = item[2]

        return output
