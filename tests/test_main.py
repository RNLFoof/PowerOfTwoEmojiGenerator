import os

from decimal import Decimal

from _pytest.monkeypatch import MonkeyPatch
from pytest import assume

from aneg import main
from aneg.main import generate_emojis, value_for_progress, enumerate_with_progress


def test_square_range():
    D = Decimal
    with assume: assert list(main.square_range(D(1), D(2))) == [1, 2]
    with assume: assert list(main.square_range(D(1), D(4))) == [1, 2, 4]
    with assume: assert list(main.square_range(D("0.5"), D(4))) == [0.5, 1, 2, 4]
    with assume: assert list(main.square_range(D("0.25"), D(4))) == [0.25, 0.5, 1, 2, 4]


def test_generate_emoji(tmp_path):
    saved_to = main.generate_emoji(Decimal("2"), 1, tmp_path)
    with assume: assert saved_to == os.path.join(tmp_path, "2.png")
    with assume: assert os.path.exists(saved_to)


def test_generate_emojis(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(
        main, "generate_emoji",
        lambda number, progress, output_directory="output":
        f"{output_directory}/{number}.png"
    )
    assert list(generate_emojis([
        Decimal(1),
        Decimal(2),
        Decimal(3),
    ])) == [
               "output/1.png",
               "output/2.png",
               "output/3.png",
           ]


def test_value_for_progress():
    assert [
        value_for_progress(0 / 3, 4, 0, 4),
        value_for_progress(1 / 3, 4, 0, 4),
        value_for_progress(2 / 3, 4, 0, 4),
        value_for_progress(3 / 3, 4, 0, 4),
    ] == [0, 1, 2, 4]


def test_enumerate_with_progress():
    with assume: assert list(enumerate_with_progress([
        1,
        11,
        111,
    ])) == [
        (0, 1),
        (1/2, 11),
        (1, 111),
    ]
    with assume: assert list(enumerate_with_progress([
        2,
        22,
        222,
        2222,
    ])) == [
        (0, 2),
        (1/3, 22),
        (2/3, 222),
        (1, 2222),
    ]
