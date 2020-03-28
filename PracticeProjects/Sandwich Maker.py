import pyinputplus as pyip


condiments = ["mayo", "mustard", "lettuce", "tomato"]
while True:
    dict = {}
    prices = {
        "chicken": 3.00,
        "turkey": 3.50,
        "ham": 3.00,
        "tofu": 4.00
    }
    cheese = ""
    bread = pyip.inputMenu(["wheat", "white", "sourdough"])
    meat = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])
    cheeseYN = pyip.inputYesNo("Would you like cheese on your sandwich? ")
    if cheeseYN == "yes":
        cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], blank=True)
    for condiment in condiments:
        dict[condiment] = pyip.inputYesNo("Would you like {} on your sandwich? ".format(condiment))
        if dict[condiment] == "no":
            del dict[condiment]
    length = len(dict.keys())
    if cheese == "":
        print("You ordered the %s sandwich on %s bread with " % (meat, bread), end="")
    else:
        print("You ordered the %s and %s sandwich on %s bread with " % (meat, cheese, bread), end="")
    for index, condiment in enumerate(dict):
        if index + 2 == length:
            print(condiment, end=" and ")
        elif index + 1 == length:
            print(condiment)
        else:
            print(condiment, end=", ")
    if pyip.inputYesNo("Is this correct? ") == "yes":
        break
count = pyip.inputInt("How many of this sandwich would you like? ", greaterThan=0)

print("%s of these will cost you $%s0" % (count, count*prices[meat]))