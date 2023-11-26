# height = float(input())
# weight = int(input())

# bmi = round(weight / (height**2), 2)

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, You are underweight!")
# elif  18.5 < bmi < 25:
#     print(f"Your bmi is {bmi}, You are Normal Weight!")
# elif 25 < bmi < 30:
#     print(f"Your bmi is {bmi}, You are Slightly overweight!")
# elif 30 < bmi < 35:
#     print(f"Your bmi is {bmi}, You are Obese.")
# else:
#     print(f"Your bmi is {bmi}, You are Clinically Obese")

#year = int(input())


# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")
# import random

# name_string = input()
# names = name_string.split(", ")
# chosen_person = names[random.randint(0, len(names)-1)]


# print(f"{chosen_person} is going to buy the meal today!")

# Nested Lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
#                "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]

# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot")
# position = input()

# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number = int(position[1])-1
# map[number][letter_index] = "X"


# print(f"{line1}\n{line2}\n{line3}\n")

# Day 4 Final Project:
# import random

# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissor = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# computer_choice = random.randint(0,2)

# options = [rock, paper, scissor]

# if user_input >= 3 or user_input < 0:
#     print("You typed an invalid number")
# else:
# # win conditions for user
#     if user_input == 0 and computer_choice == 2:
#         print(options[user_input])
#         print("Computer Chooses:")
#         print(options[computer_choice])
#         print("You win")
#     # lose conditions
#     elif computer_choice == 0 and user_input == 2:
#         print(options[user_input])
#         print("Computer Chooses:")
#         print(options[computer_choice])
#         print("You lose")

#     # lose conditions
#     elif computer_choice > user_input:
#         print(options[user_input])
#         print("Computer Chooses:")
#         print(options[computer_choice])
#         print("You lose")
#     # win conditions for user
#     elif user_input > computer_choice:
#         print(options[user_input])
#         print("Computer Chooses:")
#         print(options[computer_choice])
#         print("You Win")
#     # draw conditions
#     elif computer_choice == user_input:
#         print(options[user_input])
#         print("Computer Chooses:")
#         print(options[computer_choice])
#         print("Its a draw")

# Day 5 
# fruits = ["apple", "peach", "pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# print(fruits)
# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# for height in student_heights:
#     total_height += height

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
    
# average = round(total_height / number_of_students)

# print(f"total height = {total_height}")
# print(f"number of students = {number_of_students}")
# print(f"average height = {average}")

# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
    
# print(f"The highest score in the class is: {highest_score}")
# sum = 0
# for i in range(1, 101): # 1 till 100 -> not including 101
#     sum += i
# print(sum)
# x = int(input())
# sum = 0
# for i in range(x+1):
#     if i % 2 == 0:
#         sum += i # 2+4+6+8+10

# print(sum)
# target = int(input())
# even_sum = 0
# for number in range(2, target + 1, 2):
#     even_sum += number
# print(even_sum)

# target = 100
# for number in range(1, target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Password Generator
#Password Generator Project
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
#            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
#            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
#            'W', 'X', 'Y', 'Z']

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# l = ""

# for letter in range(nr_letters):
#     random_index = random.randint(1, len(letters) - 1)
#     l += letters[random_index]

# s = ""

# for symbol in range(nr_symbols):
#     random_index = random.randint(1, len(symbols) - 1)
#     s += symbols[random_index]

# n = ""

# for number in range(nr_numbers):
#     random_index = random.randint(1, len(numbers) - 1)
#     l += numbers[random_index]

# password = l + n + s

# final_password = "".join(random.sample(password, len(password)))
# #print(password)
# print(f"Here is your password: {final_password}")

# Day 6: Functions

# Day 7: Hangman
# import random
# import os 
# word_list = [
# 'abruptly', 
# 'absurd', 
# 'abyss', 
# 'affix', 
# 'askew', 
# 'avenue', 
# 'awkward', 
# 'axiom', 
# 'azure', 
# 'bagpipes', 
# 'bandwagon', 
# 'banjo', 
# 'bayou', 
# 'beekeeper', 
# 'bikini', 
# 'blitz', 
# 'blizzard', 
# 'boggle', 
# 'bookworm', 
# 'boxcar', 
# 'boxful', 
# 'buckaroo', 
# 'buffalo', 
# 'buffoon', 
# 'buxom', 
# 'buzzard', 
# 'buzzing', 
# 'buzzwords', 
# 'caliph', 
# 'cobweb', 
# 'cockiness', 
# 'croquet', 
# 'crypt', 
# 'curacao', 
# 'cycle', 
# 'daiquiri', 
# 'dirndl', 
# 'disavow', 
# 'dizzying', 
# 'duplex', 
# 'dwarves', 
# 'embezzle', 
# 'equip', 
# 'espionage', 
# 'euouae', 
# 'exodus', 
# 'faking', 
# 'fishhook', 
# 'fixable', 
# 'fjord', 
# 'flapjack', 
# 'flopping', 
# 'fluffiness', 
# 'flyby', 
# 'foxglove', 
# 'frazzled', 
# 'frizzled', 
# 'fuchsia', 
# 'funny', 
# 'gabby', 
# 'galaxy', 
# 'galvanize', 
# 'gazebo', 
# 'giaour', 
# 'gizmo', 
# 'glowworm', 
# 'glyph', 
# 'gnarly', 
# 'gnostic', 
# 'gossip', 
# 'grogginess', 
# 'haiku', 
# 'haphazard', 
# 'hyphen', 
# 'iatrogenic', 
# 'icebox', 
# 'injury', 
# 'ivory', 
# 'ivy', 
# 'jackpot', 
# 'jaundice', 
# 'jawbreaker', 
# 'jaywalk', 
# 'jazziest', 
# 'jazzy', 
# 'jelly', 
# 'jigsaw', 
# 'jinx', 
# 'jiujitsu', 
# 'jockey', 
# 'jogging', 
# 'joking', 
# 'jovial', 
# 'joyful', 
# 'juicy', 
# 'jukebox', 
# 'jumbo', 
# 'kayak', 
# 'kazoo', 
# 'keyhole', 
# 'khaki', 
# 'kilobyte', 
# 'kiosk', 
# 'kitsch', 
# 'kiwifruit', 
# 'klutz', 
# 'knapsack', 
# 'larynx', 
# 'lengths', 
# 'lucky', 
# 'luxury', 
# 'lymph', 
# 'marquis', 
# 'matrix', 
# 'megahertz', 
# 'microwave', 
# 'mnemonic', 
# 'mystify', 
# 'naphtha', 
# 'nightclub', 
# 'nowadays', 
# 'numbskull', 
# 'nymph', 
# 'onyx', 
# 'ovary', 
# 'oxidize', 
# 'oxygen', 
# 'pajama', 
# 'peekaboo', 
# 'phlegm', 
# 'pixel', 
# 'pizazz', 
# 'pneumonia', 
# 'polka', 
# 'pshaw', 
# 'psyche', 
# 'puppy', 
# 'puzzling', 
# 'quartz', 
# 'queue', 
# 'quips', 
# 'quixotic', 
# 'quiz', 
# 'quizzes', 
# 'quorum', 
# 'razzmatazz', 
# 'rhubarb', 
# 'rhythm', 
# 'rickshaw', 
# 'schnapps', 
# 'scratch', 
# 'shiv', 
# 'snazzy', 
# 'sphinx', 
# 'spritz', 
# 'squawk', 
# 'staff', 
# 'strength', 
# 'strengths', 
# 'stretch', 
# 'stronghold', 
# 'stymied', 
# 'subway', 
# 'swivel', 
# 'syndrome', 
# 'thriftless', 
# 'thumbscrew', 
# 'topaz', 
# 'transcript', 
# 'transgress', 
# 'transplant', 
# 'triphthong', 
# 'twelfth', 
# 'twelfths', 
# 'unknown', 
# 'unworthy', 
# 'unzip', 
# 'uptown', 
# 'vaporize', 
# 'vixen', 
# 'vodka', 
# 'voodoo', 
# 'vortex', 
# 'voyeurism', 
# 'walkway', 
# 'waltz', 
# 'wave', 
# 'wavy', 
# 'waxy', 
# 'wellspring', 
# 'wheezy', 
# 'whiskey', 
# 'whizzing', 
# 'whomever', 
# 'wimpy', 
# 'witchcraft', 
# 'wizard', 
# 'woozy', 
# 'wristwatch', 
# 'wyvern', 
# 'xylophone', 
# 'yachtsman', 
# 'yippee', 
# 'yoked', 
# 'youthful', 
# 'yummy', 
# 'zephyr', 
# 'zigzag', 
# 'zigzagging', 
# 'zilch', 
# 'zipper', 
# 'zodiac', 
# 'zombie', 
# ]
# chosen_word = random.choice(word_list)
# player_lives = 6
# end_of_game = False

# logo = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''


# print(logo)
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# #print(chosen_word)
# print(f"Psst! The chosen word is: {chosen_word}")


# display = []
# for _ in range(len(chosen_word)):
#     display += "_"

# #uessed_word = [i for i in chosen_word]


# while not end_of_game:
    
#     guess = input("Guess a letter: ").lower()
#     os.system("cls")
#     print(f"You guessed: {guess}")
    
#     for i in range(len(chosen_word)):
#         letter = chosen_word[i]
#         if  letter == guess:
#             display[i] = guess
    
#     if guess not in chosen_word:
#         print(f"'{guess}' is not in the word.")
#         player_lives -= 1
#         if player_lives == 0:
#             end_of_game = True
#             print("You lose!") 
    
#     print(f"{''.join(display)}")

#     if "_" not in display:
#         end_of_game = True
#         print("You win!")
    
#     print(stages[player_lives])

# def greet(name): # name is the parameter thats being passed in.
#   print(f"Hi! My name is {name}")
#   print("I am a Computer/Junior ML Engineer at Softech WorldWide.")

# greet("Yazdan Khan") # This is the argument for the parameter.
# import math
# test_h = int(input())
# test_w = int(input())

# coverage = 5

# def paint_calc(height = test_h, width = test_w, cover = coverage):
  
#   number_of_cans = math.ceil((height * width) / cover)

#   return number_of_cans

# no_cans = paint_calc()
# print(no_cans)

# prime number
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
  
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

# n = int(input())
# prime_checker(number=n)

# def prime_checker(number):
#   notPrime = False
#   for i in range(2, number):
#     if number % i == 0:
#       notPrime = True
      
#   if notPrime:
#     print("Its not a prime number")
#   else:
#     print("Its a prime number")
    
# prime_checker(1)

# Day 8: Caesar Cipher:
# def encrypt(text, shift):
#     text = [i for i in text]
#     print(text)
#     encrypted = ""
#     for i in range(len(text)):
#         char = text[i]
#         #print(char)
#         index_of_char = letters.index(char)
#         #print(index_of_char)
#         # if len(letters[index_of_char + shift]) > len(letters):
#         #     letters += letters
#         #     encrypted += letters[index_of_char + shift]
#         # else:
#         encrypted += letters[index_of_char + shift]
#     print(f"The encoded text is {encrypted}")


# def decrypt(text, shift):
#     text = [i for i in text].pop(" ")
#     decrypted = ""
#     for i in range(len(text)):
#         char = text[i]
#         #print(char)
#         index_of_char = letters.index(char)
#         #print(index_of_char)
#         decrypted += letters[index_of_char - shift]
#     print(f"The decoded text is {decrypted}")

# from art import logo
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(text, direction, shift):
    
#     # Variable for storing encoded or decoded message:
#     end_text = ""
#     if direction == "decode":
#         shift = -abs(shift)
        
#     for i in range(len(text)):
#         char = text[i]
#         if char in letters:
#             index_of_char = letters.index(char)
#             end_text += letters[index_of_char + shift % 26]
#         else:
#             end_text += char
#     print(f"The {direction}d text is {end_text}")


# answer = True
# while answer:
#     # print logo
#     print(logo)
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(text= text, direction= direction, shift=shift)

#     print("Do you wanna go again? 'Y' or 'N'")
#     user_inp = input()
#     if user_inp == "N":
#         print("Good Bye!")
#         answer = False

# # Day 9: Dictionaries and Nesting
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for k in student_scores:
#     if 91 <= student_scores[k] <=100:
#         student_grades[k] = "Outstanding"
#     elif  81 <= student_scores[k] <=90:
#         student_grades[k] = "Exceeds Expectations"
#     elif 71 <= student_scores[k] <=80:
#         student_grades[k] = "Acceptable"
#     else:
#         student_grades[k] = "Fail"

# print(student_grades) 

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(country, visits, list_of_cities):
#     user_dict = {}
    
#     user_dict["country"] = country
#     user_dict["visits"] = visits
#     user_dict["cities"] = list_of_cities
  
    
#     travel_log.append(user_dict)


# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# Day 9: Silent Auction Program:
# import os

# def silent_auction(name, bid):
#     # Dictionary for storing bidder's name and bid:
#     bidder_info = {
        
#     }
#     bidder_info["name"] = name
#     bidder_info["bid"] = bid
#     #print(bidder_info)
#     return bidder_info

# def bid_winner(bid_list):
#     bid_list = bid_list
#     highest_bid = 0
#     highest_bidder = ""
#     # loop for checking the highest bid
#     for i in range(len(bid_list)):
#         if bid_list[i]["bid"] > highest_bid:
#             highest_bid = bid_list[i]["bid"]
#             highest_bidder = bid_list[i]["name"]


#     print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# more_bidders = "Yes"
# bid_list = []
# while more_bidders != "No":
#     print(logo)
#     name = input("What is your name?: ")
#     bid = float(input("Enter your bid: $"))
#     more_bidders = input("Are there more bidders? Type 'Yes' or 'No': ")
    
#     if more_bidders == "Yes":
#         os.system('cls')
#     else:
#         bid_winner(bid_list=bid_list)
#     bid_list.append(silent_auction(name, bid))

# Day 10: Functions with output:

# def format_name(f_name, l_name):
#     full_name = f"{f_name} {l_name}"
    
#     return full_name.title()

# formatted_fullname = format_name('muhammad', 'obaid')

# print(formatted_fullname)

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
#     if is_leap(year=year) and month == 2:
#         return 29
#     else:
#         days = month_days[month - 1]
    
#     return days


# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

# Calculator:

# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b


# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }

# def calc(a, b, operation):
    
#     calc_function = operations[operation]
#     answer = calc_function(a, b)
#     return answer
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
# |_____________________|
# """
# def calculator():
#     print(logo)
#     a = float(input("Enter a number: "))
#     continue_ = True
#     while continue_:
#         b = float(input("Enter another number: "))
#         operation = input("Enter operation: ")
#         answer = calc(a, b, operation)
#         print(f'{a} {operation} {b} = {answer}')
        
#         resume = input(f"Type y to continue calcculating with {answer}, or type n to start a new calculation")
        
#         if resume == "y":
#             a = answer
#         elif resume == "n":
#             continue_ = False
#             calculator() # This code is calling the function again and this concept is known as recursion.

# calculator()

# Black Jack:

# def black_jack():
#     us_inp = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
#     if us_inp == 'y':
#         player_hand = deal_card()
#         player_sum = 0
#         for i in player_hand:
#             player_sum += i
            
#         computer_hand = deal_card()
#         computer_first_card = computer_hand[0]
#         computer_sum = 0
#         for i in computer_hand:
#             computer_sum += i
        
        
#         print(f"Player's hand: {player_hand}, current_score: {player_sum}")
#         print(f"Computer's first card: {computer_first_card}")
    
#     conti = input("Type 'y' to get another card, type 'n' to pass: ")    
#     if  conti == "y":
#         player_hand += random.choices(deck_of_cards, k = 1)
#         player_sum += player_hand[-1]
#         print(f"Player's hand: {player_hand}, current_score: {player_sum}")
#         print(f"Computer's first card: {computer_first_card}")
        
#         if player_sum > 21:
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")            
#             print("You went over! You lose")
#         elif player_sum == 21 or player_sum > computer_sum:
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")
#             print("You win!")
#         elif (player_sum > computer_sum) and (player_sum < 21):
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")            
#             print("Computer wins")
#     elif conti == "n":
#         if computer_sum > 21:
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")            
#             print("You went over! You lose")
#         elif computer_sum == 21 or computer_sum > player_sum:
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")
#             print("You win!")
#         elif (computer_sum > player_sum) and (computer_sum < 21):
#             print(f"Player's final hand: {player_hand}, current_score: {player_sum}")
#             print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")            
#             print("Computer wins")
            
            
# black_jack()
# import random
# import os

# def deal_card():
#     deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#     hand = random.choice(deck_of_cards)
#     return hand

# def calculate_score(cards):
    
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Draw "
#     elif computer_score == 0:
#         return "Lose, opponent has  Blackjack"
#     elif user_score == 0:
#         return "Win with a Blackjack"
#     elif user_score > 21:
#         return "You went over. You lose"
#     elif computer_score > 21:
#         return "Opponent went over. You win"
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose"

# def play_game():
#     logo = """
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |                
#       `------'                           |__/           
# """
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
        
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True    
#         else:
#             user_input = input("Type y to get another card, type 'n' to pass: ")
#             if user_input == 'y':
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f" Your final hand: {user_cards}, final score: {user_score}")
#     print(f" Computer final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of BJ type y or no: ") == "y":
#     os.system('cls')
#     play_game()

# Day 12

################### SCOPE #######################
# enemies = 1

# def increase_enemies():
    
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope: Exists within functions

# def drink_potion():
#     potion_strength = 2

# Number Guessing Game:
# import random

# EASY_LEVEL = 10
# HARD_LEVEL = 5

# def set_difficulty():
#     user_input = input("Choose a difficulty level: hard or easy: ")
    
#     if user_input == "hard":
#         return HARD_LEVEL
#     else:
#         return EASY_LEVEL

# def check_answer(random_number, guess, turns):
    
#     if guess > random_number:
#         print("Too high!")
#         turns -= 1
#     elif guess < random_number:
#         print("Too low.")
#         turns -= 1
#     elif guess == random_number:
#         print(f"You win you guessed the number: {random_number}")

#     return turns
# def game():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     random_number = random.randint(1,100)
    
#     turns = set_difficulty()
    
#     # Repeat the guessing functionality.
#     guess = 0
#     while guess != random_number:
#         #print(turns)
#         print(f"You have {turns} attempts left to guess the number.")
#         # let the user guess a number
#         guess = int(input("Make a guess: "))
        
#         # Track the number of turns and reduce by 1 if they get it wrong.
#         turns = check_answer(random_number=random_number, turns=turns, guess=guess)
        
#         if turns == 0:
#             print("You are out of guesses. You lose!")
#             return 
#         elif guess != random_number:
#             print("Guess again")
    
# game()
# Day 13: Debugging
# Day 14: Higher Lower Game:

# """ 
# Problem Definition:
# 1. pick 2 random accounts and display their info (display follower count of only 1 account)
# 2. Ask the user to guess if the follower count of the other account is higher or lower.
# 3. A function that compares to check if the guess is right, right = increase score else game over
# 4. A function for repeatability of the program
# """
# from game_data import data
# import random
# import os

# def format_data(account):
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
    
#     return f"{account_name}, a {account_descr}, from {account_country}."

# def check_answer(guess, a_followers, b_followers):
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"


# score = 0
# game_should_continue = True
# account_b = random.choice(data)

# while game_should_continue:
#     account_a = account_b
#     account_b = random.choice(data)

#     while account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format_data(account_a)}")
#     print(f"Against B: {format_data(account_b)}")

#     guess = input("Who has more followers? type 'A' or 'B': ").lower()

#     a_follower_count = account_a['follower_count']
#     b_follower_count = account_b['follower_count']

#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     os.system('cls')

#     if is_correct:
#         score += 1
#         print(f'youre right, current_score:{score}')
#     else:
#         print(f"ur wrong, current_score:{score}")
#         game_should_continue = False
    
# Day 15: Coffee Machine

# def report(resources, money):
#     return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
        
# def check_resources(ingredients_of_drink):
    
#     for ingredient in ingredients_of_drink:
#         resources_available = resources[ingredient]
#         resource_required = ingredients_of_drink[ingredient]
        
#         if resources_available >= resource_required:
#             return True
#         else:
#             print(f"Sorry there is not enough {ingredient}")
#             return False

# def make_coffee(total, drink_cost, ingredients_of_drink):
    
#     for ingredient in ingredients_of_drink:
#         resources_available = resources[ingredient]
#         resource_required = ingredients_of_drink[ingredient]
        
#         if (resources_available >= resource_required) and (total >= drink_cost):
#             resources[ingredient] = resources_available - resource_required
#             change = total - drink_cost
        
    
#     return resources, round(change, 2)

# def check_cost():
#     quarters = int(input("How many quarters?: "))
#     dimes = int(input("How many dimes?: "))
#     nickles = int(input("How many nickles?: "))
#     pennies = int(input("How many pennies?: "))
#     total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    
#     return total
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# money = 0.0
# ask_again = False
# while not ask_again:
    
#     user_input = input("What would you like? (espresso/latte/cappucino):")
    
#     if user_input == "report":
#         print(report(resources, money))
#     elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
#         ingredients_of_drink = MENU[user_input]["ingredients"]
#         cost_of_drink = MENU[user_input]["cost"]
#         if check_resources(ingredients_of_drink):
#             payment = check_cost()
#             if payment >= cost_of_drink:
#                 resources, change = make_coffee(payment, cost_of_drink, ingredients_of_drink)
#                 money += cost_of_drink
#                 #print(resources)
#                 print(f"Here is your ${change} change")
#                 print(f"Here is your {user_input}")
#             else:
#                 print("Sorry not enough money. Money refunded")

#     elif user_input == "off":
#         ask_again = True

# Day 16: OOP
from turtle import Turtle, Screen
from prettytable import PrettyTable



# timmy = Turtle()
# my_screen = Screen()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)
# timmy.circle(120)
# timmy.forward(50)
# timmy.circle(120)

# my_screen.exitonclick()

# table = PrettyTable()
# pokemon_name = ['Pikachu', 'Squirtle', 'Charmander']
# types = ["Electric", "Water", "Fire"]
# table.add_column('Pokemon Name', column= [i for i in pokemon_name])
# table.add_column('Type', column= [i for i in types])
# table.align = 'r'
# print(table)

# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine


# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()

# ask_again = False
# while not ask_again:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}):")
    
#     if choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     elif choice == "off":
#         ask_again = True
#     else:
#         drink = menu.find_drink(choice)
        
#         if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
#                 coffee_maker.make_coffee(drink)

# Day 17: Object Oriented Programming:
"""Creating our own classes in OOP"""

# PascalCase - camelCase - snake_case

# class User:
#     def __init__(self, user_id, name) -> None: # This function is called everytime a new object is created.
#         self.id = user_id
#         self.username = name 
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

#         return user.followers
# user_1 = User(1, 'Angela')
# user_2 = User(2, "Ozair")

# user_1.follow(user_2)

# print(user_1.followers)
# print(user_1.following)

# print(user_2.followers)
# print(user_2.following)

# Day 18:
import turtle as t
import random


screen = Screen()
t.colormode(255)
t.hideturtle()

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
def random_color(color_list):
    random_color = random.choice(color_list)
    return random_color

def draw_spots():
    t.speed('fastest')
    t.begin_fill()
    t.circle(radius=10)
    t.penup()
    t.fd(50)
    t.pendown()
    t.end_fill()

def set_pos(x, y):
    t.penup()
    return t.setpos(x, y)

x, y = -200, -200
spots = 10
while spots != 0:
    set_pos(x, y)
    for _ in range(10):
        t.color(random_color(color_list))
        y += 5
        draw_spots()
    set_pos(x, y)
    spots -= 1

screen.exitonclick()
