# letters = 'Ozair'
# new_list = [i*2 for i in range(1, 6)]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# short_names= [name.upper() for name in names if len(name) >= 5]
# print(short_names)


# list_of_strings = input().split(',')

# even_numbers = [num for num in list_of_strings if int(num) % 2 == 0]
# print(even_numbers)

with open('file1.txt', 'r') as f:
    data1 = f.read().split('\n')
    
with open('file2.txt', 'r') as f:
    data2 = f.read().split('\n')

result = [int(str1) for str1 in data1 if str1 in data2]

print(result)

