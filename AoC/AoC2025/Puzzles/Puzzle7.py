from puzzleBase import PuzzleBase

class Puzzle7(PuzzleBase):
    def get_test_data(test_data):
        return """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    def solve_part1(self) -> str:
        lines = self.get_puzzle_input().strip().splitlines()
        grid = [list(line) for line in lines]
        start = grid[0].index('S')
        grid[1][start] = '|'

        row_above = grid[1]
        splits = 0
        for row in range(1, len(grid)):
            for col in range(len(grid[row])):
                if row_above[col] == '|':
                    if grid[row][col] == '.':
                        grid[row][col] = '|'
                    elif grid[row][col] == '^':
                        splits += 1
                        if (col - 1 >= 0):
                            grid[row][col-1] = '|'
                        if (col + 1 < len(grid[row])):
                            grid[row][col+1] = '|'
            row_above = grid[row]
        
        # for row in range(len(grid)):
        #     print(''.join(grid[row]))

        return str(splits)

    def solve_part2(self) -> str:
        lines = self.get_puzzle_input().strip().splitlines()
        grid = [
            list(line)
            for index, line in enumerate(lines, start=1)
            if index % 2 == 1
        ]

        start = grid[0].index('S')

        result = Puzzle7.find_timeline(0, start, grid)

        for row in range(len(grid)):
            print(''.join(grid[row]))

        return str(result)

    @staticmethod
    def find_timeline(row: int, col: int, grid: list[list[str]]) -> int:
        #grid[row][col] = '|'
        if len(grid) -1 == row:
            return 1

        next_row = grid[row+1]
        if next_row[col] == '.':
            return Puzzle7.find_timeline(row + 1, col, grid)
        if next_row[col] == '^':
            return Puzzle7.find_timeline(row + 1, col - 1, grid) + Puzzle7.find_timeline(row + 1, col + 1, grid)
        
