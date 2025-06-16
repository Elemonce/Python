import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("parentheses", [
                         "()",
                         "(())",
                         "(()(()))"])
def test_matching_parentheses(parentheses):
    assert matching_parentheses(parentheses)

@pytest.mark.parametrize("parentheses", [
    ")())(())",
    "())()(()))",
    "())(()))"
])
def test_not_matching_parentheses(parentheses):
    assert not matching_parentheses(parentheses)