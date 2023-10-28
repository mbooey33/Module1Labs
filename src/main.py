print("Hello World")
print("My Name is Mac")
print("I am 26 years old")
print("This is my first Python code")

# Calculate Whitworth's age
yearWhitworth = 1890
ageWhitworth = 2023 - yearWhitworth
print('Whitworth is ' + str(ageWhitworth) + ' years old')

# question 1
# Integer variables
int_var1 = int(input("Enter an integer value for int_var1: "))
int_var2 = int(input("Enter an integer value for int_var2: "))
int_var3 = int(input("Enter an integer value for int_var3: "))

# Float variables
float_var1 = float(input("Enter a float value for float_var1: "))
float_var2 = float(input("Enter a float value for float_var2: "))
float_var3 = float(input("Enter a float value for float_var3: "))

# Perform arithmetic operations on integers
int_addition = int_var1 + int_var2
int_subtraction = int_var1 - int_var2
int_multiplication = int_var1 * int_var2
int_division = int_var1 / int_var2
int_modulus = int_var3 % int_var2

# Perform arithmetic operations on floats
float_addition = float_var1 + float_var2
float_subtraction = float_var1 - float_var2
float_multiplication = float_var1 * float_var2
float_division = float_var1 / float_var2

# Display the results
print("Arithmetic operations on integers:")
print("Addition:", int_addition)
print("Subtraction:", int_subtraction)
print("Multiplication:", int_multiplication)
print("Division:", int_division)
print("Modulus:", int_modulus)

print("\nArithmetic operations on floats:")
print("Addition:", float_addition)
print("Subtraction:", float_subtraction)
print("Multiplication:", float_multiplication)
print("Division:", float_division)


# Get the bill amount from the user
bill_amount = float(input("Enter the bill amount: $"))

# Tip percentages
tip_percentages = [0.10, 0.15, 0.20, 0.25]

# Calculate and display tip and total for each predetermined percentage
for tip_percentage in tip_percentages:
    tip = bill_amount * tip_percentage
    total = bill_amount + tip
    print(f'Tip ({tip_percentage * 100}%): ${tip:.2f}, Total Bill: ${total:.2f}')

# Ask the user for a custom tip percentage
custom_tip_percentage = float(input("Enter your custom tip percentage (e.g., 18% as 0.18): "))

# Calculate and display tip and total for the custom percentage
custom_tip = bill_amount * custom_tip_percentage
custom_total = bill_amount + custom_tip
print(f'Custom Tip ({custom_tip_percentage * 100}%): ${custom_tip:.2f}, Total Bill: ${custom_total:.2f}')


# Initialize variables to hold game point totals
game1 = float(input("Enter the points for game 1: "))
game2 = float(input("Enter the points for game 2: "))
game3 = float(input("Enter the points for game 3: "))
game4 = float(input("Enter the points for game 4: "))
game5 = float(input("Enter the points for game 5: "))

# Calculate the total points
total_points = game1 + game2 + game3 + game4 + game5

# Calculate the average points per game
num_games = 5  # Total number of games
average_points_per_game = total_points / num_games

# Print the average points per game
print(f"Average points per game: {average_points_per_game:.2f}")

# Define hourly rate and number of hours worked
hourly_rate = 16.5  # Dollar amount per hour
hours_worked = float(input("Enter the number of hours worked this week: "))

# Calculate the regular pay and overtime pay
if hours_worked <= 40:
    regular_pay = hours_worked * hourly_rate
    overtime_pay = 0.0
else:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * (hourly_rate * 1.5)

# Question 7
# Calculate the total weekly pay
weekly_pay = regular_pay + overtime_pay

# Display the results
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Weekly Pay: ${weekly_pay:.2f}")

# Question 8
# Ask the user for their name
user_name = input("Enter your name: ")

# Display a welcome message
print(f"Welcome, {user_name}!")

# Question 9
# Ask the user for inputs
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
past_tense_verb = input("Enter a past-tense verb: ")
noun2 = input("Enter another noun: ")

# Create and display the mad lib phrase
mad_lib_phrase = f"The quick, {adjective} {noun1} {past_tense_verb} over the lazy {noun2}."
print(mad_lib_phrase)

# Question 10
# Ask the user for inputs
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
past_tense_verb = input("Enter a past-tense verb: ")
adverb = input("Enter an adverb: ")
adjective2 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")

#madlib story
my_mad_lib_phrase = f"Today I went to the zoo. I saw a(n) {adjective} {noun1} jumping up and down in its tree. He {past_tense_verb} {adverb} through the large tunnel that lead to its {adjective2} {noun2}."
print(my_mad_lib_phrase)

# Question 11

# Ask the user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if num2 is not equal to 0 before performing division and modulus
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
    print("Division:", division)
    print("Modulus:", modulus)
else:
    print("Division and Modulus: You can't divide by 0.")

# Display the results of addition, subtraction, and multiplication
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# Question 12

# Ask the user for their age
age = int(input("Enter your age: "))

# Check age and provide corresponding output
if age < 0:
    print("Invalid age")
elif age >= 55:
    print("You get the senior discount")
elif age >= 21:
    print("You can enjoy a beer")
elif age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")

# Question 13

import random

# Get the user's choice
user_choice = input("Enter 1 (rock), 2 (paper), or 3 (scissors): ")

# Convert the user's choice to an integer
user_choice = int(user_choice)

# Check if the user's choice is valid
if user_choice not in [1, 2, 3]:
    print("Invalid choice. Please choose 1 (rock), 2 (paper), or 3 (scissors).")
else:
    # Generate a random choice for the computer
    computer_choice = random.randint(1, 3)

    # Define the choices
    choices = {1: "rock", 2: "paper", 3: "scissors"}

    # Display the user's choice and the computer's choice
    print(f"Your choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        print("You win!")
    else:
        print("Computer wins!")
