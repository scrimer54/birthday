from datetime import date, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_year = today.year
    current_weekday = today.weekday()
    days_until_next_monday = (7 - current_weekday) % 7
    next_monday = today + timedelta(days=days_until_next_monday)

    birthdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    all_birthday_passed = True

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        if birthday.year < current_year:
            birthday_this_year = birthday.replace(year=current_year + 1)
        elif birthday.year > current_year:
            birthday_this_year = birthday.replace(year=current_year)
        else:
            birthday_this_year = birthday

        if birthday_this_year > today:
            all_birthday_passed = False

        days_until_birthday = (birthday_this_year - today).days % 365

        for day_offset in range(7):
            next_birthday = today + timedelta(days=day_offset)

            if next_birthday.weekday() == 5: 
                next_birthday += timedelta(days=2)  
            elif next_birthday.weekday() == 6:  
                next_birthday += timedelta(days=1)  

            if days_until_birthday == day_offset:
                if next_birthday >= today:
                    day_name = next_birthday.strftime("%A")
                    birthdays[day_name].append(name)

    if all_birthday_passed:
        return {}

    return {day_name: names for day_name, names in birthdays.items() if names}
    

if __name__ == "__main__":
    users = [
        {"name": "Biba", "birthday": date(2023, 1, 1)},
        {"name": "Boba", "birthday": date(2023, 9, 12)},
        {"name": "Ivan", "birthday": date(2023, 9, 17)},
        {"name": "Igor", "birthday": date(2023, 9, 16)},
        {"name": "Vasil", "birthday": date(2023, 9, 15)},
        
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")