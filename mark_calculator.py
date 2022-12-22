# Prompt the user to enter the number of points they have achieved
achievedPoints = int(input("How many points did you get?\t\t"))

# Prompt the user to enter the maximum number of points that can be achieved
maxPoints = int(input("What are the max points you can get?\t\t"))

# Calculate the student's mark using the formula
yourMark = ((achievedPoints * 5) / maxPoints) + 1

# Round the mark to 2 decimal places
yourMark = round(yourMark, 2)

# Print the student's mark
print(f"You have the mark of {yourMark}")