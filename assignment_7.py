"""
COMP 163 - Introduction to Programming
Assignment: Assignment 7 - Course Schedule Formatter
Name: Kahlil Batieste
GitHub Username: kahlilb7
Date: February 23, 2026
Description: This program reads course registration data entered by the user,
cleans and formats each field, detects scheduling conflicts, and prints a
professional course schedule.
AI Usage: None
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting
# ============================================================

courses = []

while True:
    line = input().strip()

    if line == "DONE":
        break

    parts = line.split("|")

    code = parts[0].strip()
    title = parts[1].strip()
    days = parts[2].strip()
    time = parts[3].strip()
    room = parts[4].strip()

    
    code_parts = code.split()
    dept = code_parts[0].upper()
    num = code_parts[1]
    code = dept + " " + num

    
    courses.append([code, title, days, time, room])


# ============================================================
# Step 2: Title and Room Formatting
# ============================================================

for course in courses:
    course[1] = course[1].title()
    course[4] = course[4].title()

# ============================================================
# Step 3: Day Code Expansion
# ============================================================

for course in courses:
    days_code = course[2].upper()
    full_days = []

    for character in days_code:
        if character == "M":
            full_days.append("Monday")
        elif character == "T":
            full_days.append("Tuesday")
        elif character == "W":
            full_days.append("Wednesday")
        elif character == "R":
            full_days.append("Thursday")
        elif character == "F":
            full_days.append("Friday")

    course[2] = "/".join(full_days)

# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
