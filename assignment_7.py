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

   
    if len(parts) != 5:
        continue

    code_raw = parts[0].strip()
    title_raw = parts[1].strip()
    days_raw = parts[2].strip()
    time_raw = parts[3].strip()
    room_raw = parts[4].strip()

    
    code_parts = code_raw.split()
    dept = code_parts[0].upper() if len(code_parts) > 0 else ""
    num = code_parts[1] if len(code_parts) > 1 else ""
    code_clean = (dept + " " + num).strip()

    
    courses.append([code_clean, title_raw, days_raw, time_raw, room_raw])


# ============================================================
# Step 2: Title and Room Formatting
# ============================================================


# ============================================================
# Step 3: Day Code Expansion
# ============================================================


# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
