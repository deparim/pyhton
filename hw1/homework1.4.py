# 4

user_var = int(input('Please enter a positive integer: '))

i = user_var
max = i % 10

while i > 0:
    if i % 10 > max:
        max = i % 10
    i = i // 10
print(max)





