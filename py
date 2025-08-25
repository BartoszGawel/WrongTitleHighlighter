import openpyxl
from openpyxl.styles import PatternFill

# Download excel file
workbook = openpyxl.load_workbook("File Source")  #Change to source of your file e.g. C:\\File.xlsx
sheet = workbook.active

# Step 1: Count the occurrences of positions in column B.
job_counts = {}
for row in sheet.iter_rows(min_row=2, min_col=2, max_col=2):
    job_title = row[0].value
    if job_title:
        job_counts[job_title] = job_counts.get(job_title, 0) + 1

# Step 2: Create a dictionary of positions that appear at least twice
repeated_jobs = {job: count for job, count in job_counts.items() if count >= 2} # If You can in this place You can set e.g. 3x in dictionary

# Step 3: Mark in red the positions that are not in the dictionary.
red_fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid') #Here You can change Your color.

for row in sheet.iter_rows(min_row=2, min_col=2, max_col=2):
    job_title = row[0].value
    if job_title and job_title not in repeated_jobs:
        row[0].fill = red_fill

# Save the modified file
workbook.save('newfile.xlsx') #You can change the name of Your file
print("We made it!")
