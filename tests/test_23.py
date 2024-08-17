import pytest
import leetcode.leetcode_23 as solver

testcases = [
    (
        [solver.to_linked_list(x) for x in [[1, 2, 3], [3, 4, 5], [2, 55]]],
        solver.to_linked_list([1, 2, 2, 3, 3, 4, 5, 55]),
    ),
    (
        [solver.to_linked_list(x) for x in [[1, 2, 3], [3, 4, 5], []]],
        solver.to_linked_list([1, 2, 3, 3, 4, 5]),
    ),
]


@pytest.mark.parametrize("param,expected", testcases)
def test_23(param: list[solver.ListNode], expected: solver.ListNode):
    sol = solver.Solution()
    result = sol.mergeKLists(param)
    while result:
        assert result.val == expected.val
        result = result.next
        expected = expected.next
