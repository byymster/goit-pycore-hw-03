import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or quantity <= min or quantity >= max:
        raise ValueError('Invalid input')

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)


if __name__ == '__main__':
    try:
        min = int(input('Enter min number: '))
        max = int(input('Enter max number: '))
        quantity = int(input('Enter quantity of numbers: '))
        print(get_numbers_ticket(min, max, quantity))
    except ValueError as e:
        print('Invalid input')
        print([])
