import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import random
import json
import subprocess
import os

# Load items from JSON file
with open('items.json') as file:
    items_data = json.load(file)

problems = {}
language = "java"

for i in range(len(items_data)):
    item = {
        'Problem': items_data[i]['Problem'],
        'Difficulty': items_data[i]['Difficulty'],
        'Group': items_data[i]['Group'],
        'javaLink': items_data[i]['javaLink'],
        'pythonLink': items_data[i]['pythonLink']
    }
    problems[i] = item

def open_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code_text.delete('1.0', tk.END)  # Clear the current content
            code_text.insert(tk.END, file.read())  # Display the content of the file
    except FileNotFoundError:
        code_text.delete('1.0', tk.END)
        code_text.insert(tk.END, "File not found!")
        print(file_path)

def randomize_question():
    selected_question = random.choice(list(problems.values()))

    print("Problem:", selected_question['Problem'])
    print("Difficulty:", selected_question['Difficulty'])
    print("Group:", selected_question['Group'])
    print(" ")
    file_path = selected_question['javaLink']
    if language == "python":
        file_path = selected_question['pythonLink']
    directory = os.getcwd()
    file = os.path.join(directory, file_path)
    open_python_file(file)

# Create the main application window
root = tk.Tk()
root.title("Python File Viewer")

# Create a ScrolledText widget to display the Python code
code_text = ScrolledText(root, wrap=tk.WORD, font=("Courier", 12))
code_text.pack(fill=tk.BOTH, expand=True)

# Create a button to randomize the question
randomize_button = tk.Button(root, text="Randomize Question", command=randomize_question)
randomize_button.pack()

# Start the main event loop
root.mainloop()
