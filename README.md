# Student Mark Calculator
This Python code calculates and prints out a student's mark based on the number of points they have achieved out of the maximum number of points that can be achieved.

## How the program works
The code starts by prompting the user to enter the number of points they have achieved, which is stored in the variable achievedPoints. It then prompts the user to enter the maximum number of points that can be achieved, which is stored in the variable maxPoints.

The code then calculates the student's mark using the formula yourMark = ((achievedPoints * 5) / maxPoints) + 1. This formula scales the student's achieved points to a 5-point scale (where the maximum number of points corresponds to a mark of 5) and adds 1 to the result to get the student's mark.

They next line of code rounds the student's mark to 2 decimal places using the round function

Finally, the code prints out the student's mark using the print function.