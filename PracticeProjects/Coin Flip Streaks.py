import random
numberOfStreaks = 0
for experimentNumber in range(10000):  # 10000 sets of 100 coin flips
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipArray = []
    inARow = 1
    for x in range(100):
        flipArray.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index, flip in enumerate(flipArray):
        if index > 0 and flip == flipArray[index - 1]:
            inARow += 1
        else:
            inARow = 1
        if inARow == 6:
            numberOfStreaks += 1


print("total streaks of 6+ of same side: " + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))