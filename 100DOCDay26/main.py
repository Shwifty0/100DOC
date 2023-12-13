# letters = 'Ozair'
# new_list = [i*2 for i in range(1, 6)]

#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# short_names= [name.upper() for name in names if len(name) >= 5]
# print(short_names)


# list_of_strings = input().split(',')

# even_numbers = [num for num in list_of_strings if int(num) % 2 == 0]
# print(even_numbers)

# with open('file1.txt', 'r') as f:
#     data1 = f.read().split('\n')
    
# with open('file2.txt', 'r') as f:
#     data2 = f.read().split('\n')

# result = [int(str1) for str1 in data1 if str1 in data2]

# print(result)

# Dictionary Comprehension
# import random

# student_scores = {student:random.randint(1,100) for student in names}

# passed_students = {students:marks for (students, marks) in student_scores.items() if marks > 50}
# print(passed_students)

import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_code = {row.letter:row.code for (index, row) in data.iterrows()}

userinp = input('Enter a Name:')

def nato_code_generator(input):
    result = [nato_code[char.upper()] for char in userinp]
    return result

result = nato_code_generator(userinp)
print(result)