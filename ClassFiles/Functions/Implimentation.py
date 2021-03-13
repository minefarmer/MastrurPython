## Functions

# print("Welcome to the program, what is your name?")
# name_result = input("Enter your response here -> ")
# print(f"Your response was {name_result}")  # Your response was Enter your response here -> rich

# print("What did you think of the food you ate today?")
# food_result = input("Enter your response here -> ")
# print(f"Your response was {food_result}")  # Your response was great

# print("What tv show ending did you dislike the most ever?")
# show_result = input("Enter your response here -> ")
# print(f"Your response was {show_result}")  # Your response was got



def get_input_from_user():
    return input("Enter your response here ->")

print("Welcome to the program, what is your name?")
name_result = get_input_from_user()  # Enter your response here -> carl

print("What did you think of the food you ate today?")
food_result = get_input_from_user()  # Enter your response here -> great

print("What tv show ending did you dislike the most ever?")
show_result = get_input_from_user()  # Enter your response here -> got

print(f"To summarize: Your name is {name_result.capitalize()}. you ate {food_result} food today and hated the ending of {show_result.upper()}")  # To summarize: Your name is Carl. you ate great food today and hated the ending of GOT
