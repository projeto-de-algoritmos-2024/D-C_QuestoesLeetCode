"""
Problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
Dificulty: hard
Solved: True
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def to_linked_list(l: list[int]):
    result: list[ListNode] = []

    for item in l:
        if not result:
            v = ListNode(item)
            result.append(v)
            continue

        v = ListNode(item)
        result[-1].next = v
        result.append(v)

    if not result:
        return None

    return result[0]


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]
        h: list[tuple[int, int, ListNode]] = []
        result = []
        occ = 0
        for l in lists:
            heapq.heappush(h, (l.val, occ, l))
            occ += 1

        while h:
            value, _, linked_list = heapq.heappop(h)
            result.append(value)

            if linked_list.next:
                linked_list = linked_list.next
                heapq.heappush(h, (linked_list.val, occ, linked_list))
                occ += 1

        return to_linked_list(result)


if __name__ == "__main__":
    a = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # a = [[]]
    _input = []
    for item in a:
        root = to_linked_list(item)
        _input.append(root)

    sol = Solution()
    result = sol.mergeKLists(_input)
    print(result)
