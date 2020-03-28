import sys


def collatz(number):  # runs the collatz sequence
    if number % 2 == 0:
        new = number // 2
        print(str(new))
        return new
    else:
        new = 3 * number + 1
        print(str(new))
        return new

count = 1

while True:
    try:
        choice = int(input("Enter an integer to start collatz sequence: "))
    except ValueError:
        print("You must enter an integer.")
        continue
    num = choice  # set user's choice as the first value in collatz sequence
    print(num)
    while True:
        num = collatz(num)
        count += 1
        if num == 1:
            print("there were " + str(count) + " numbers in your sequence")
            break
    if input("Create another sequence? (Y/N)") == "Y":
        count = 1
        continue
    else:
        print("Goodbye")
        break

