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
    ...

def enumerate_with_progress(numbers: list[float]) -> Generator[tuple[float, float], None, None]:
    ...

def main():
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
