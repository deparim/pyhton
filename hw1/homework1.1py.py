#1

var_dig1 = 1
var_dig2 = 2
var_dig3 = 3
var_srt = 'This variable is a word'
var_srt2 = 'This variable is also a word'

print(var_dig1, var_dig2, var_dig3)
print(var_srt)
print(var_srt2)

user_dig = input('Choose a digital variable: ')
user_dig2 = input('Choose another digital variable: ')
user_dig3 = input('Choose the last digital variable: ')

print(f'The user chose the following digital variables: {user_dig}, {user_dig2}, {user_dig3}.')

user_str = str.format(input('Now choose a string variable: '))
user_str2 = str.format(input('Now choose another string variable: '))
user_str3 = str.format(input('Now choose the last string variable: '))

print(f'The user chose the following string variables: {user_str}, {user_str2}, {user_str3}.')
