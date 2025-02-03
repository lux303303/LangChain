import pytest
from src import github_actions


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(2, "even", id="positive_even"),
        pytest.param(3, "odd", id="positive_odd"),
        pytest.param(0, "even", id="zero"),
        pytest.param(-1, "odd", id="negative_odd"),
        pytest.param(-2, "even", id="negative_even")
    ]
)
def test_is_even_or_odd(n, expected):
    assert github_actions.is_even_or_odd(n) == expected
