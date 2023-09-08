from datetime import date, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_weekday = today.weekday()
    days_until_next_monday = (7 - current_weekday) % 7
    next_monday = today + timedelta(days=days_until_next_monday)

    birthdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Sunday": [],
    }

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        if birthday < today:
            next_birthday = date(today.year + 1, birthday.month, birthday.day)
        else:
            next_birthday = birthday

        days_until_birthday = (next_birthday - today).days

        for day_offset in range(7):
            next_birthday = today + timedelta(days=day_offset)

            if next_birthday.weekday() == 5:  # Якщо день тижня - субота
                next_birthday += timedelta(days=2)  # Переносимо на понеділок наступного тижня
            elif next_birthday.weekday() == 6:  # Якщо день тижня - неділя
                next_birthday += timedelta(days=1)  # Переносимо на понеділок наступного тижня

            if days_until_birthday == day_offset:
                if next_birthday > today:  # Перевірка, чи день народження в майбутньому
                    if next_birthday.weekday() == 0:  # Якщо вихідний на понеділок
                        birthdays["Monday"].append(name)
                    elif next_birthday.weekday() == 1:  # Якщо вихідний на вівторок
                        birthdays["Tuesday"].append(name)
                    elif next_birthday.weekday() == 2:  # Якщо вихідний на середу
                        birthdays["Wednesday"].append(name)
                    elif next_birthday.weekday() == 3:  # Якщо вихідний на четвер
                        birthdays["Thursday"].append(name)
                    elif next_birthday.weekday() == 4:  # Якщо вихідний на п'ятницю
                        birthdays["Friday"].append(name)
                    elif next_birthday.weekday() == 6:  # Якщо вихідний на неділю
                        birthdays["Sunday"].append(name)

    all_birthday_passed = all(birthday < today for user in users)
    all_weekend = all(date.weekday() in [5, 6] for date in [next_monday, next_monday + timedelta(days=1),
                                                             next_monday + timedelta(days=2), next_monday + timedelta(days=3),
                                                             next_monday + timedelta(days=4)])

    if all_birthday_passed or all_weekend:
        return {}

    return birthdays
    

if __name__ == "__main__":
    users = [
        {"name": "Biba", "birthday": date(2023, 9, 13)},
        {"name": "Boba", "birthday": date(2023, 9, 12)},
        {"name": "Ivan", "birthday": date(2023, 9, 11)},
        {"name": "Igor", "birthday": date(2023, 9, 9)},
        {"name": "Vasil", "birthday": date(2023, 9, 10)},
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")


