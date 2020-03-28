import re

password = input("Enter a strong Password: ")

capRegex = re.compile(r"[A-Z]")
lowRegex = re.compile(r"[a-z]")
numRegex = re.compile(r"\d")
regexes = capRegex, lowRegex, numRegex

for regex in regexes:
    if regex.search(password) == None or len(password) < 8:
        print('Come on, that was weak.')
        exit()
print("Nice password!")