tableData = [['apples', 'oranges', 'cherries', 'banana', "plum"],
             ['Alice', 'Bob', 'Carol', 'David', "Eric"],
             ['dogs', 'cats', 'moose', 'goose', "platypus"]]


def printTable(tableData):
    colWidth = len(tableData[0])
    rowHeight = len(tableData)
    longest = 0
    newData = []
    for col in range(colWidth):
        for row in range(rowHeight):
            itemLength = len(tableData[row][col])
            if itemLength > longest:
                longest = itemLength
    for col in range(colWidth):
        for row in range(rowHeight):
            newData.append([])
            spacing = longest + 1
            newData[col].append(tableData[row][col])
            item = newData[col][row]
            print(item.rjust(spacing, " "), end="")
        print()


printTable(tableData)
