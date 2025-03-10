from datetime import datetime, timedelta


def check_if_bday_in_next_year(
    birthday: datetime.date, today_date: datetime.date
) -> bool:
    date_in_next_year = birthday.replace(year=today_date.year + 1)
    days_to_birthday = (date_in_next_year - today_date).days
    return 0 <= days_to_birthday < 7


def check_weekend(date: datetime.date) -> int:
    match date.isoweekday():
        case 6:
            return 2
        case 7:
            return 1
        case _:
            return 0


def get_upcoming_birthdays(users: list) -> list:
    today_date = datetime.today().date()
    # today_date = datetime.strptime("2024.12.27", "%Y.%m.%d").date()
    # today_date = datetime.strptime("2024.01.22", "%Y.%m.%d").date()
    # TODO remove all prints
    print(f"Today: {today_date}")

    congrat_list = []
    congrats_date = None

    for user in users:
        birthday_data_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_data_obj.replace(year=today_date.year)

        if birthday_this_year < today_date:
            birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

        days_until_birthday = (birthday_this_year - today_date).days

        if 0 <= days_until_birthday < 7:
            congrats_date = birthday_this_year + timedelta(
                days=check_weekend(birthday_this_year)
            )

            congrat_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congrats_date.strftime("%Y.%m.%d"),
                }
            )
    return congrat_list


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice Cooper", "birthday": "1990.06.16"},
        {"name": "Bob Dylan", "birthday": "1990.01.02"},
        {"name": "Axl Rose", "birthday": "1990.01.01"},
        {"name": "Sid Vicious", "birthday": "1990.01.03"},
        {"name": "Bob Marley", "birthday": "1990.12.30"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
