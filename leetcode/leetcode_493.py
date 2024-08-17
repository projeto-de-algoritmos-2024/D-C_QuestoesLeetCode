"""
Problem: https://leetcode.com/problems/reverse-pairs/
Dificulty: hard
Solved: True
"""

from typing import List


class Solution:
    def merge(self, left: list[int], right: list[int]):
        i = 0
        j = 0
        result = []
        count = 0

        for item in left:
            while j < len(right) and item > 2 * right[j]:
                j += 1
            count += j

        j = 0
        while i < len(left) and j < len(right):
            a = left[i]
            b = right[j]
            if a <= b:
                result.append(a)
                i += 1
            else:
                result.append(b)
                j += 1

        if i < len(left):
            result += left[i:]

        if j < len(right):
            result += right[j:]

        return count, result

    def merge_count(self, arr: list[int]):
        if len(arr) <= 1:
            return 0, arr

        mid = len(arr) // 2
        left_count, left_sorted = self.merge_count(arr[:mid])
        right_count, right_sorted = self.merge_count(arr[mid:])
        total_count, total_sorted = self.merge(left_sorted, right_sorted)

        return (total_count + right_count + left_count), total_sorted

    def reversePairs(self, nums: List[int]) -> int:
        counted, _ = self.merge_count(nums)
        return counted


if __name__ == "__main__":
    a = [1, 3, 2, 3, 1]
    # a = [-5, -5]
    sol = Solution()
    count = sol.reversePairs(a)
    print(count)
