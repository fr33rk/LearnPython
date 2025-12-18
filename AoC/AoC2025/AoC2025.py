from puzzleBase import RunMode as RU
from Puzzle6 import Puzzle6

currentPuzzle = Puzzle6()

currentPuzzle.RunMode = RU.TEST

print("Part 1:", currentPuzzle.solve_part1())
print("Part 2:", currentPuzzle.solve_part2())