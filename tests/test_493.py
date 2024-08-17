import pytest
import leetcode.leetcode_493 as solver

testcases = [
    ([1, 3, 2, 3, 1], 2),
    ([2, 4, 3, 5, 1], 3),
    ([1, 3, 1, 4, 1, 10, 4], 4),
]


@pytest.mark.parametrize("param,expected", testcases)
def test_493(param: list[int], expected: int):
    sol = solver.Solution()
    result = sol.reversePairs(param)
    assert result == expected
