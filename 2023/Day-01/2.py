f = open('input.txt', 'r')
summa = 0


def find_number(txt: str):
    numbers = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    result = []
    ln = len(txt)
    i = 0

    while i < ln:
        for key in numbers.keys():
            key_ln = len(key)

            if i + key_ln <= ln and txt[i:i + key_ln] == key:
                result.append(numbers[key])
                break

        i += 1

    return result[0] * 10 + result[-1]


for line in f:
    summa += find_number(line)
    print(find_number(line))

print(summa)
