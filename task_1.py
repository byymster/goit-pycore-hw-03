from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()
    difference = date_obj - today
    return difference.days


if __name__ == '__main__':
    while True:
        date = input('Enter a date in the format YYYY-MM-DD: ')
        if date == 'exit':
            break
        try:
            print(f'Difference in day from today: {get_days_from_today(date)}')
            break
        except ValueError:
            print('Invalid date format. Please try again.')
