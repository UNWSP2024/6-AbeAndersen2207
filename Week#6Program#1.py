#UNWSP Programming PythonCos2005DEsp25
#Week#5_Program#1_Random Dice
#02/28/2025
#Abraham. N. Andersen


import random  # We need this to make our dice rolls random!

def randDice():
  """
  This function simulates rolling two dice and returns their sum.
  """
  # Roll the first die (a random number between 1 and 6)
  die1 = random.randint(1, 6)
  # Roll the second die (another random number between 1 and 6)
  die2 = random.randint(1, 6)
  # Add the two dice rolls together
  total = die1 + die2
  # Give back the total to whoever called the function
  return total

# Main part of the program
total_rolls = 100  # We'll roll the dice 100 times
sum_of_rolls = 0  # We'll keep track of the total sum of all the rolls

# Let's roll those dice!
for i in range(total_rolls):
  # Call the randDice function and store the result
  roll_result = randDice()
  # Add the result to the total sum
  sum_of_rolls += roll_result
  #print(f"Roll {i + 1}: {roll_result}") #if you want to see each roll

# Calculate the average roll
average_roll = sum_of_rolls / total_rolls

# Round the average to two decimal places (nearest 0.01)
rounded_average = round(average_roll, 2)

# Print the result
print(f"After rolling two dice {total_rolls} times, the average roll was: {rounded_average}")