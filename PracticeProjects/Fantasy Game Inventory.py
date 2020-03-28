

inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print(" Inventory ".center(40, "="))
    item_total = 0
    for k, v in inventory.items():
        print(("%s %s" % (v, k)).rjust(40))  # string interpolation
    item_total = sum(inventory.values())
    print(f"\nTotal number of items: {item_total}\n")  # f-string


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0)
        inventory[item] += 1


displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
