def is_armstrong_number(number):
    total = 0
    length = len(str(number))

    for num in str(number):
        total += int(num) ** length

    if total == number:
        return True
    else:
        return False
