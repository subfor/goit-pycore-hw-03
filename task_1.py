from datetime import datetime


def get_days_from_today(date: str) -> int:
    today_date = datetime.now()
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    delta = today_date - date_obj
    return delta.days


if __name__ == "__main__":
    print(get_days_from_today("2028-10-10"))
    print(get_days_from_today("2020-10-10"))
