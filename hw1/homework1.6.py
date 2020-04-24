# 6

a = float(input('Enter start: '))
b = float(input('Enter finish: '))
n = 1

i = a
print(f'Day {n}: {i} km')

while i <= b:
    i = i * 1.1
    n = n + 1
    print(f'Day {n}: {i} km')
    if i > b:
        print(f'By the day {n} the man ran no less than {b} kms')
        break
