import re
from puzzleBase import PuzzleBase

class Puzzle1(PuzzleBase):
    def get_test_data(self):
        return """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    
    def solve_part1(self) -> str:
        puzzle_input = self.get_puzzle_input().strip()

        position = 50
        max_position = 100
        puzzle_result = 0

        regexp = re.compile("(?P<Direction>L|R)(?P<Count>\\d+)")
        steps = regexp.findall(puzzle_input)

        for step in steps:
            direction = step[0]
            count = int(step[1]) % 100

            if direction == "L":
                position -= count
            elif direction == "R":
                position += count

            if position < 0:
                position += 100
            elif position >= 100:
                position -= 100

            if (position == 0): 
                puzzle_result += 1
        return str(puzzle_result)

    def solve_part2(self) -> str:
        puzzle_input = self.get_puzzle_input().strip()

        position = 50
        puzzle_result = 0
        for line in puzzle_input.splitlines():
            tours, count = divmod(int(line[1:]), 100)
            puzzle_result += tours
            started_at_zero = (position == 0)
            if line[0] == "L": 
                count *= -1
            position += count

            if (position == 0):
                puzzle_result += 1
            elif position < 0:
                if not started_at_zero:
                    puzzle_result += 1
                position += 100           
            elif position >= 100:
                position -= 100
                if not started_at_zero:
                    puzzle_result += 1

            print(f"{position}:{puzzle_result}")

        return str(puzzle_result)