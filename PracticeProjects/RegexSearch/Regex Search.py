import re
from pathlib import Path
import os

p = Path(os.getcwd())  # path to current working directory
txtRegex = re.compile(r"\.txt")
txtFiles = []
fileContents = []
# check for .txt files in cwd
for file in os.listdir(p):
    if txtRegex.search(file):
        txtFiles.append(file)
# store contents of each file in list
for file in txtFiles:
    x = open(file)
    contents = x.read()
    fileContents.append(contents)
    x.close()

userInput = input("Enter a regex to search the .txt files in this directory: ")
regex = re.compile(userInput)
# finds matches in file contents and prints result
for index, content in enumerate(fileContents):
    matches = regex.findall(content)
    print("file {} matches: {}".format(str(index + 1), matches))
