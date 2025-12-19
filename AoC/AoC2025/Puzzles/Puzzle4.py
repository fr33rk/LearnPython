from puzzleBase import PuzzleBase
import copy

class Puzzle4(PuzzleBase):
    def get_test_data(test_data):
        return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    directions = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

    def solve_part1(self):
        rows = self.get_puzzle_input().strip().split('\n')
        row_count = len(rows)
        col_count = len(rows[0])
        result = 0
        for row in range(row_count):
            for col in range(col_count):
                if (rows[row][col] == '.'):
                    continue
                roll_count = 0
                for direction in self.directions:
                    if row + direction[1] < 0 or row + direction[1] > row_count - 1 or col + direction[0] < 0 or col + direction[0] > col_count - 1:
                        pass
                    elif rows[row + direction[1]][col + direction[0]] == '@':
                        roll_count += 1
                        if roll_count == 4:
                            break
                if roll_count < 4:
                    print(f"Found lonely roll at {row},{col} with {roll_count} neighbors")
                    result += 1
        return result
    
    def remove_rolls(self, input: list[list[str]], row_count:int, col_count:int) -> tuple[list[list[str]], int]:
        output = copy.deepcopy(input)
        removed_rolls = 0
        for row in range(row_count):
            for col in range(col_count):
                if (input[row][col] == '.'):
                    continue
                roll_count = 0
                for direction in self.directions:
                    if row + direction[1] < 0 or row + direction[1] > row_count - 1 or col + direction[0] < 0 or col + direction[0] > col_count - 1:
                        pass
                    elif input[row + direction[1]][col + direction[0]] == '@':
                        roll_count += 1
                        if roll_count == 4:
                            break
                if roll_count < 4:
                    output[row][col] = "."
                    removed_rolls += 1

        return output, removed_rolls

    def solve_part2(self):
        rows = [list(line) for line in self.get_puzzle_input().strip().split('\n')]
        row_count = len(rows)
        col_count = len(rows[0])
        total_rolls_removed = 0
    
        result = [rows, 0]
        while True:
            result = self.remove_rolls(result[0], row_count, col_count)
            if result[1] == 0:
                break
            total_rolls_removed += result[1]
        return total_rolls_removed

