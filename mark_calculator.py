# The points you've earned
achievedPoints = int(input("How many points did you get?\t\t"))

# The maximum points you can actually get
maxPoints = int(input("What are the max points you can get?\t\t"))

# Calculates your mark using formula
yourMark = ((achievedPoints * 5) / maxPoints) + 1

# Output of calculated mark
print(f"You have the mark of {yourMark:.2f}")