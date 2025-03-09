import random


def get_numbers_ticet(min: int, max: int, quantity: int) -> list:
    if min >= 1 and max <= 1000 and quantity <= max:
        return sorted(random.sample(range(min, max + 1), quantity))
    else:
        return []


if __name__ == "__main__":
    print(get_numbers_ticet(1, 5, 5))
    print(get_numbers_ticet(1, 5, 3))
    print(get_numbers_ticet(1, 5, 23))
