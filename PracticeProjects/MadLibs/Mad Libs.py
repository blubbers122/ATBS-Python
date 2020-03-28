import pyinputplus as pyip
import re


adj = pyip.inputStr("Enter an adjective: ")
noun1 = pyip.inputStr("Enter a noun: ")
verb = pyip.inputStr("Enter a past-tense verb: ")
noun2 = pyip.inputStr("Enter a noun: ")

nouns = [noun1, noun2]

adjRegex = re.compile(r"ADJECTIVE")
nounRegex = re.compile(r"NOUN")
verbRegex = re.compile(r"VERB")

libFile = open("lib.txt", "r")
lib = libFile.read()
libFile.close()

newLib = adjRegex.sub(adj, lib)  # swaps ADJECTIVE
for i in range(2):
    newLib = nounRegex.sub(nouns[i], newLib, 1)  # swaps both NOUNs
newLib = verbRegex.sub(verb, newLib)  # swaps VERB
print(newLib)

newLibFile = open("newlib.txt", "w")
newLibFile.write(newLib)
newLibFile.close()

