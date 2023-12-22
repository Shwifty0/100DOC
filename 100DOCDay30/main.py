# # File not found

# try:
#     file = open("a_file.txt")
#     dictionary = {'a':1}
#     print(dictionary['b'])
# except FileNotFoundError as error:
#     print(f"There was {error} message, therefore creating a new file.")
#     file = open('a_file.txt', 'w')
# except KeyError as key:
#     print(f"The key:{key} was not found in the dictionary.")

height = float(input('Height:'))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError('Human Height should not be over 3 meters')

print(f"The bmi is {weight / height ** 2}")