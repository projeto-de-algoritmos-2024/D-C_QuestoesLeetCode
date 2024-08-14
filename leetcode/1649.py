"""
Problem: https://leetcode.com/problems/create-sorted-array-through-instructions/
Difficulty: hard
Solved: True
"""

from typing import List, Callable


class Solution:

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        i = 0
        j = 0

        result = []
        while i < len(left) and j < len(right):
            a = left[i][0]
            b = right[j][0]
            if a <= b:
                result.append(left[i])
                i += 1
            else:
                right[j][2] += len(left) - i  # Get  biggest elements
                result.append(right[j])
                j += 1

        if i < len(left):
            result = result + left[i:]

        if j < len(right):
            result = result + right[j:]

        return result

    def merge_reverse(self, left: list[int], right: list[int]) -> list[int]:
        i = 0
        j = 0

        result = []
        while i < len(left) and j < len(right):
            a = left[i][0]
            b = right[j][0]
            if a >= b:
                result.append(left[i])
                i += 1
            else:
                right[j][1] += len(left) - i  # Get smallest elements
                result.append(right[j])
                j += 1

        if i < len(left):
            result = result + left[i:]

        if j < len(right):
            result = result + right[j:]

        return result

    def do_thing(
        self,
        entry: list[tuple[int, int, int]],
        merge_func: Callable[[list[int], list[int]], list[int]],
    ) -> list[int]:
        if len(entry) <= 1:
            return entry

        mid = len(entry) // 2
        left = entry[:mid]
        right = entry[mid:]

        sorted_left = self.do_thing(left, merge_func)
        sorted_right = self.do_thing(right, merge_func)
        sorted_final = merge_func(sorted_left, sorted_right)

        return sorted_final

    def createSortedArray(self, instructions: List[int]) -> int:
        to_sort = []
        for item in instructions:
            to_sort.append([item, 0, 0])

        _ = self.do_thing(to_sort, self.merge)
        _ = self.do_thing(to_sort, self.merge_reverse)
        count = 0
        for item in to_sort:
            smaller = item[1]
            bigger = item[2]
            cost = min(smaller, bigger)
            count += cost

        return count % (10**9 + 7)
