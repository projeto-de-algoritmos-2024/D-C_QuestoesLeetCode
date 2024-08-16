"""
Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
Dificulty: hard
Solved: True
"""

from typing import List


class Solution:

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        i = 0
        j = 0

        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i < len(left):
            result = result + left[i:]

        if j < len(right):
            result = result + right[j:]

        return result

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        mid = (len(merged) - 1) // 2
        if len(merged) & 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid + 1]) / 2


if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    sol = Solution()
    print(a + b)
    print(sol.findMedianSortedArrays(a, b))
