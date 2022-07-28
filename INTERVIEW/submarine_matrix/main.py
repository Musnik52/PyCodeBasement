# INSTRUCTIONS:
# In a given a matrix as a "water-space", a submarine's location is marked by X.
# IF some Xs are adjecent (horizontally, vertycally or both) - they're considered as one submarine.
# Surrounding a submatine can only be an empty space (or 0), or the borders of the matrix.
# Write a program to identify how many submarines there are in the given matrix.
# Include a short explanation & tests.

class Solution():

    # if not in the grid
    def submarine_count(self, grid):
        if len(grid) == 0:
            return 0

        # check for sub location
        rows_length = len(grid)
        col_length = len(grid[0])
        sub_sum = 0
        for row in range(rows_length):
            for col in range(col_length):
                if grid[row][col] == "x":
                    sub_sum += 1
                self.check_adjecent(row, col, rows_length, col_length, grid)
        return sub_sum

    def check_adjecent(self, row, col, rows_length, col_length, grid):
        if row < 0 or col < 0 or row >= rows_length or col >= col_length:
            return  # makes sure the search is within boundries
        if grid[row][col] == "0":
            return
        else:
            grid[row][col] = "0"  # recurrsion stopper
            self.check_adjecent(row + 1, col, rows_length,
                                col_length, grid)  # check right space
            self.check_adjecent(row - 1, col, rows_length,
                                col_length, grid)  # check left space
            self.check_adjecent(row, col + 1, rows_length,
                                col_length, grid)  # check above
            self.check_adjecent(row, col - 1, rows_length,
                                col_length, grid)  # check below


if __name__ == "__main__":

    # answer = 5
    grid = [["x", "x", "0", "x", "0"],
            ["0", "0", "0", "x", "0"],
            ["0", "0", "0", "0", "0"],
            ["x", "0", "0", "x", "x"],
            ["0", "0", "0", "x", "x"],
            ["0", "x", "0", "x", "x"]]

    #answer = 4
    # grid = [["x", "x"],
    #         ["x", "x"],
    #         ["0", "0"],
    #         ["0", "x"],
    #         ["0", "0"],
    #         ["0", "0"],
    #         ["0", "x"],
    #         ["0", "x"],
    #         ["0", "0"],
    #         ["x", "x"]]

    #answer = 1
    # grid = [["x", "x", "x"]]

    #answer = 0
    # grid = [["0", "0", "0"],
    #         ["0", "0", "0"],
    #         ["0", "0", "0"]]

    boris = Solution()
    print(boris.submarine_count(grid))
