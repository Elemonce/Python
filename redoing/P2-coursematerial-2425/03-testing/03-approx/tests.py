import pytest
from mystatistics import average


@pytest.mark.parametrize("expected, actual", [
    [0.1, [0.1, 0.1, 0.1]],
    [4, [2, 3, 7]]
])


def test_average(expected, actual):
    assert pytest.approx(expected, abs=0.01) == average(actual)
