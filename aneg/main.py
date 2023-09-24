from decimal import Decimal
from typing import Generator, Sequence


def square_range(lowest: Decimal, highest: Decimal) -> Generator[Decimal, None, None]:
    at = lowest
    while at <= highest:
        yield at
        at *= 2


def generate_emoji(number: Decimal, progress: float, output_directory="output") -> str:
    ...


def generate_emojis(numbers: Sequence[Decimal], output_directory="output") -> str:
    ...

def value_for_progress(progress: float, number_of_values: int,  value_at_no_progress: float,
                       value_at_max_progress: float) -> float:
    # This is set up in a way that uses the sequence 0, 1, 2, 4... instead of the more consistent 0.5, 1, 2, 4...
    # But it ensures that both the lowest and highest provided values are both placed somewhere.
    # Maybe change it someday to use a consistent curve that actually hits both??
    if progress == 0:
        return 0
    progress_delta = value_at_no_progress + value_at_max_progress
    at_nth_item = int(progress * (number_of_values - 1))
    return value_at_no_progress + (
        progress_delta * (
            (2 ** at_nth_item) /
            (2 ** (number_of_values - 1))
        )
    )

def enumerate_with_progress(numbers: list[float]) -> Generator[tuple[float, float], None, None]:
    ...

def main():
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
