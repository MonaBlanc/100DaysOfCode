# ############DEBUGGING#####################

# # Describe Problem
# #The range ends at 19 in this function, if you want to include 20, you need to change the range to 1, 21
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# # We start at 0 and not 1 so we need to change the range to 0, 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# # We need to catch the 1994 year, so we need to change the if statement to include 1994
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # We need to indent the print statement and change the input to an integer the f is missing too
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# #
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #we need to switch the == to = to avoid the comparison
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# #print(f"pages = {pages}")
# #print(f"word_per_page = {word_per_page}")
# print(total_words)

# #Use a Debugger
# #We indent the list outside of the for loop
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])