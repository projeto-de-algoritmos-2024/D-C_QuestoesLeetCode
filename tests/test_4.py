import pytest
import leetcode.leetcode_4 as solver

testcases = [
    ([1, 3], [2], 2.0000),
    ([40, 50, 60], [1, 7], 40.0000),
    ([1, 2], [3, 4], 2.5000),
]


@pytest.mark.parametrize("param1,param2,expected", testcases)
def test_4(param1: list[int], param2: list[int], expected: int):
    sol = solver.Solution()
    result = sol.findMedianSortedArrays(param1, param2)
    assert result == expected
