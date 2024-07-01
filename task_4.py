from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    upcoming_birthdays = []
    today = datetime.now()
    for user in users:
        birthday_this_year = datetime.strptime(f'{today.year}.{user["birthday"][5:]}', "%Y.%m.%d")
        difference = (birthday_this_year - today).days

        if 0 <= difference <= 7:
            # If the birthday falls on a weekend, shift it to the next Monday
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


if __name__ == '__main__':
    users = [
        {'name': 'Vasyl Vasylovych', 'birthday': '1990.01.01'},
        {'name': 'Ivan Ivanov', 'birthday': '1991.02.02'},
        {'name': 'Petro Petrov', 'birthday': '1992.03.03'},
        {'name': 'Oleg Oleynik', 'birthday': '1993.04.04'},
        {'name': 'Andriy Andriyenko', 'birthday': '1994.05.05'},
        {'name': 'Serhiy Serhiyenko', 'birthday': '1995.06.06'},
        {'name': 'July Julivna', 'birthday': '1996.07.05'},
        {'name': 'Dmytro Dmytrenko', 'birthday': '1996.07.07'},
        {'name': 'Maksym Maksymenko', 'birthday': '1989.07.06'},
        {'name': 'Oleksandr Oleksandrenko', 'birthday': '1997.08.08'},
        {'name': 'Mykola Mykolenko', 'birthday': '1998.09.09'},
        {'name': 'Yuriy Yuriyenko', 'birthday': '1999.10.10'},
        {'name': 'Taras Tarasenko', 'birthday': '2000.11.11'},
        {'name': 'Roman Romanenko', 'birthday': '2001.12.12'},
    ]

    for user in get_upcoming_birthdays(users):
        print(f"Congratulate {user['name']} on {user['congratulation_date']}")