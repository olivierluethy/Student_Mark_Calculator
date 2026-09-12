# Student Mark Calculator

A tiny command-line Python script that converts a test score into a Swiss-style
grade (1–6). Enter the points you achieved and the maximum points, and it prints
your mark.

## How it works

The grade is calculated with the standard linear formula:

```
mark = (achievedPoints * 5) / maxPoints + 1
```

This scales your points onto the 1–6 scale, where the maximum score maps to a 6,
and rounds the result to two decimal places.

## Tech

- Python 3 (standard library only)

## Run

```bash
python mark_calculator.py
```

You'll be prompted for the points you achieved and the maximum points, and the
resulting mark is printed.

## Files

```
mark_calculator.py                    # the script
formula_for_calculation_of_mark.png   # the grading formula, illustrated
```
