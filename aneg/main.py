from decimal import Decimal
from typing import Generator


def square_range(lowest: Decimal, highest: Decimal) -> Generator[Decimal, None, None]:
    at = lowest
    while at <= highest:
        yield at
        at *= 2

def main(name):
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
