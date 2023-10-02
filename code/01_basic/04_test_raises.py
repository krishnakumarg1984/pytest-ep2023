import pytest
from rpncalc.utils import calc


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc(3, 0, "/")
