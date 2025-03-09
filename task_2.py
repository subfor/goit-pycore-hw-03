import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if 1 <= min <= max <= 1000 and quantity <= (max - min + 1):
        return sorted(random.sample(range(min, max + 1), quantity))
    return []


if __name__ == "__main__":
    print(get_numbers_ticket(1, 5, 3))
    print(get_numbers_ticket(1, 5, 5))
    print(get_numbers_ticket(1, 5, 23))
    print(get_numbers_ticket(100, 5, 5))
    print(get_numbers_ticket(10, 15, 10))
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
