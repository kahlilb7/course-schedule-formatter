# Course Schedule Formatter

## Overview
This project reads course registration data, cleans and formats each field, detects scheduling conflicts, and outputs a structured course schedule.

## Features
- Parses user input using `|`
- Cleans course codes, titles, and rooms
- Expands day abbreviations (MW → Monday/Wednesday)
- Standardizes time format (9:00am → 9:00 AM)
- Detects scheduling conflicts
- Outputs a formatted schedule

## How to Run
```bash
python course_schedule_formatter.py

Enter course data in this format:

code|title|days|time|room

Type DONE when finished.

Project Background

This project was originally completed as part of a Computer Science course and later refined for portfolio use.

Future Improvements
Add input validation
Improve user interaction
Convert logic into functions