spam = ["apples", "bananas", "tofu", "cats", "frogs", "cows"]
empty = []

def Commator(list):
    string = ""
    for index, item in enumerate(list):
        if index == len(list) - 1:
            string += "and " + item
        else:
            string += item + ", "
    return string


print(Commator(empty))
print(Commator(spam))
