grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def nestLoop(grid):
    for x in range(len(grid[0])):  # for every x index in grid (6 repeats in this case)
        for y in range(len(grid)):  # for every y index in grid (9 repeats in this case)
            print(grid[y][x], end="")  # prints the entire y column on one line
        print()  # skips to next line for next y column


def zipAndMap(grid):
    print("\n".join(map("".join, zip(*grid))))


nestLoop(grid)  # uses nested for loop

# zip transposes the grid diagonally, each row is joined to one string,
# then the rows are joined separated by new lines
zipAndMap(grid)
