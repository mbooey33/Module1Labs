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

# Calculate the total weekly pay
weekly_pay = regular_pay + overtime_pay

# Display the results
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Weekly Pay: ${weekly_pay:.2f}")
