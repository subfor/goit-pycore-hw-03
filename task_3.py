import re


def normalize_phone(phone_number: str) -> str:
    pattern = r"[^\d+]"
    cleaned_number = re.sub(pattern, "", phone_number.strip())
    match cleaned_number:
        case number if number.startswith("0"):
            return f"+38{number}"
        case number if number.startswith("38"):
            return f"+38{cleaned_number}"
        case _:
            return cleaned_number


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
