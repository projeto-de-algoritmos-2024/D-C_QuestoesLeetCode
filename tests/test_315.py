import pytest
import leetcode.leetcode_315 as solver

testcases = [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1], [0]), ([-1, -1], [0, 0])]


@pytest.mark.parametrize("param,expected", testcases)
def test_315(param: list[int], expected: list[int]):
    sol = solver.Solution()
    result = sol.countSmaller(param)
    assert result == expected
