"""
Course Schedule Formatter

This program reads course data, cleans and formats each field,
detects scheduling conflicts, and outputs a structured schedule.

Features:
- Input parsing and cleaning
- Day expansion (MW → Monday/Wednesday)
- Time formatting
- Conflict detection
- Formatted schedule output

Author: Kahlil Batieste
"""

# --- Input Parsing & Course Code Formatting ---

courses = []

# Collect courses until user types DONE

while True: 
    line = input().strip()

    if line == "DONE":
        break

# Split input into its 5 parts using |

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


# --- Title and Room Formatting ---

for course in courses:
    course[1] = course[1].title()
    course[4] = course[4].title()

# --- Day Code Expansion ---

# Loop through each character since days 
# are stored as combined letters like "MWF"
for course in courses:
    days_code = course[2].upper()
    full_days = []

# Convert compressed day codes like MW into full day names

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

# --- Time Standardization ---

# Split time into clock part and AM/PM, then format consistently

for course in courses:
    time = course[3].strip().lower()

    am_pm = time[-2:].upper()
    clock = time[:-2]

    course[3] = clock + " " + am_pm

# --- Conflict Detection ---

conflicts = []

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        code1 = courses[i][0]
        code2 = courses[j][0]

        days1 = courses[i][2].split("/")
        days2 = courses[j][2].split("/")

        time1 = courses[i][3]
        time2 = courses[j][3]
                                
  # Compare each pair of courses to check for conflicts
                                
        shared_days = []
        for day in days1:
            if day in days2:
                shared_days.append(day)

        if len(shared_days) > 0 and time1 == time2:
            conflicts.append(code1 + " and " + code2 + " conflict on " +
                             ", ".join(shared_days) + " at " + time1)

# --- Output & Formatted Printing ---

print("=== AGGIE COURSE SCHEDULE ===")
print()

# Align output into fixed-width columns for clean printing

for i in range(len(courses)):
    course = courses[i]
    print("COURSE " + str(i + 1) + ":")
    print("  Code:  " + course[0])
    print("  Title: " + course[1])
    print("  Days:  " + course[2])
    print("  Time:  " + course[3])
    print("  Room:  " + course[4])
    print()

print("=== SCHEDULE SUMMARY ===")
print("Total courses: " + str(len(courses)))
print()

print("=== CONFLICT REPORT ===")
if len(conflicts) == 0:
    print("No conflicts detected.")
else:
    for c in conflicts:
        print(c)
print()

print("=== FORMATTED FOR PRINTING ===")
for course in courses:
    code = course[0].ljust(10)
    title = course[1].ljust(26)
    time = course[3].ljust(11)

    abbreviations = course[2]
    abbreviations = abbreviations.replace("Monday", "Mon")
    abbreviations = abbreviations.replace("Tuesday", "Tue")
    abbreviations = abbreviations.replace("Wednesday", "Wed")
    abbreviations = abbreviations.replace("Thursday", "Thu")
    abbreviations = abbreviations.replace("Friday", "Fri")
    abbreviations = abbreviations.ljust(13)

    print(code + title + abbreviations + time + course[4])
