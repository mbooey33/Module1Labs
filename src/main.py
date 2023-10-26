print("Hello World")
print("My Name is Mac")
print("I am 26 years old")
print("This is my first Python code")

# Calculate Whitworth's age
yearWhitworth = 1890
ageWhitworth = 2023 - yearWhitworth
print('Whitworth is ' + str(ageWhitworth) + ' years old')

# question 2
# Integer variables
int_var1 = 15
int_var2 = 7
int_var3 = 20

# Float variables
float_var1 = 10.5
float_var2 = 3.2
float_var3 = 8.0

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


# question 2
# Bill amount
bill_amount = 47.56

# Tip percentages
tip_percentages = [0.10, 0.15, 0.20, 0.25]

# Calculate tip and total for each percentage
for tip_percentage in tip_percentages:
    tip = bill_amount * tip_percentage
    total = bill_amount + tip
    print(f'Tip ({tip_percentage * 100}%): ${tip:.2f}, Total Bill: ${total:.2f}')


# question 3
# Point totals for each game
game1 = 13
game2 = 18
game3 = 21
game4 = 17
game5 = 31

# Calculate the total points
total_points = game1 + game2 + game3 + game4 + game5

# Calculate the average points per game
num_games = 5  # Total number of games
average_points_per_game = total_points / num_games

# Print the average points per game
print(f"Diana's average points per game: {average_points_per_game}")
