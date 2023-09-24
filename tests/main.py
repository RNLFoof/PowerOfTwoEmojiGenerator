import pytest
from decimal import Decimal
from pytest import assume

from aneg.main import square_range


def test_square_range():
    D = Decimal
    with assume: assert list(square_range(D(1), D(2))) == [1, 2]
    with assume: assert list(square_range(D(1), D(4))) == [1, 2, 4]
    with assume: assert list(square_range(D("0.5"), D(4))) == [0.5, 1, 2, 4]
    with assume: assert list(square_range(D("0.25"), D(4))) == [0.25, 0.5, 1, 2, 4]