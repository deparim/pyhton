# 2

user_time_sec = int(input('Please enter the time in seconds: '))

time_hours = user_time_sec // 3600
remainder = user_time_sec % 3600
time_min = remainder // 60
time_sec = remainder % 60

print(f'The time is: {time_hours}:{time_min}:{time_sec}')
