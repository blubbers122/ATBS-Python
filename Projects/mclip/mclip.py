#! python3
# mclip.py - A multi-clipboard program.
import pyperclip
import pyinputplus as pyip
import shelve


def clipper():
    while True:
        mcbShelf = shelve.open("mcb")
        commands = mcbShelf["commands"]
        text = mcbShelf["text"]
        mcbShelf.close()
        print('enter keyword to copy contents or "c" to see commands')
        keyphrase = input("Enter keyword or command: ")
        if keyphrase.lower() == "c":
            print("\ncommands:\nThe current saved clips are:\n")
            for item in text.items():
                print(item)
            print()
            for command in list(commands.items()):
                print(str(command[0]) + ": " + str(command[1]))
        elif keyphrase.lower() == "a":
            mcbShelf = shelve.open("mcb", writeback=True)
            key = pyip.inputStr("Enter the keyword that you will use to call your new clip: ")
            clip = input("Now enter your clip for " + key + ": ")
            mcbShelf["text"][key] = clip
            print(key + " clip added!")
            mcbShelf.close()
        elif keyphrase.lower() == "d":
            print("choose one of the following to delete or enter 'e' to escape.")
            for key in text:
                print(key.center(38))
            while True:
                keyEntry = input()
                if keyEntry in text or keyEntry.lower() == "e":
                    break
            if keyEntry in text:
                print("deleting %s key..." % keyEntry)
                mcbShelf = shelve.open("mcb", writeback=True)
                del mcbShelf["text"][keyEntry]
                mcbShelf.close()
            else:
                clipper()
        else:
            break
    if keyphrase in text:
        pyperclip.copy(text[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
    else:
        if pyip.inputYesNo('There is no text for ' + keyphrase + '\nWould you like to try again? ') == "yes":
            clipper()


clipper()
