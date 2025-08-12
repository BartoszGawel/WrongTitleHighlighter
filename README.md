# WrongTitleHighlighter
This Python script processes an Excel file and highlights job titles or similar titles in column B (could be any) that appear less than twice by marking them in red. It’s useful for identifying outliers or inconsistencies in job title data.

📦 Requirements
Python 3.x
openpyxl library
Install openpyxl if you don’t have it yet:


🚀 How to Use
Clone or download this repository.
Run the script using any Python environment (e.g. Jupyter Notebook, VS Code, terminal).
When prompted, enter:
The full path to your Excel file (e.g. C:/Users/YourName/Documents/jobs.xlsx)
The desired name and path for the output file (e.g. C:/Users/YourName/Documents/highlighted_jobs.xlsx)

📄 What It Does
Reads job titles from column B (starting from row 2) - of course could be any other column in my case it was the second.
Counts how many times each title appears - this thing is to create a dictionary. 
Highlights titles that appear only once in red. For what? Because I will now that some titles are not common so I need to check it, seriously it is or its just wrong wrote.
Saves the modified file to the location you specify.

🛠️ Customization
You can modify the script to:
Change the column being analyzed.
Adjust the minimum number of repetitions required. - in my case I choose only 2 times, for better dictionary You can crete with 3x.
Use different highlight colors.

📁 File Format
Make sure your Excel file is in .xlsx format and contains job titles in column B.
