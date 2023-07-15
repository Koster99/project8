from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    day_now = today.weekday()
    days_head = (0 - day_now + 7) % 7
    next_monday = today + timedelta(days=days_head)
    date_after_seven_days = today + timedelta(days=8)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Next Monday': []
    }

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%d-%m-%Y').date()
        birthday_without_year = birthday.replace(year=today.year)
        if today <= birthday_without_year <= date_after_seven_days:
            if day_now in [5, 6] and (birthday_without_year - today).days < 2: # якщо сьогодні вихідний і різниця між днем нарожедння і сьогодні не більше 1 для - то в понеділок треба
                birthdays_per_week['Monday'].append(user['name'])
            elif birthday_without_year.weekday() >= 5:  # Вихідні дні
                birthdays_per_week['Next Monday'].append(user['name'])
            else:
                birthdays_per_week[birthday_without_year.strftime('%A')].append(user['name'])

    for day, birthdays in birthdays_per_week.items():
        if birthdays:
            print(f"{day}: {', '.join(birthdays)}")


people = [
    {'name': 'Bill', 'birthday': '16-07-2000'},
    {'name': 'David', 'birthday': '18-07-2002'},
    {'name': 'Jill', 'birthday': '19-07-1999'},
    {'name': 'Alex', 'birthday': '20-07-2000'},
    {'name': 'Petro', 'birthday': '22-07-2002'},
    {'name': 'Sergiy', 'birthday': '17-07-1999'}
]

if __name__ == '__main__':
    get_birthdays_per_week(people)
