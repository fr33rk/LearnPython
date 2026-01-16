from puzzleBase import RunMode as RU
from Puzzles.Puzzle7 import Puzzle7
import time

currentPuzzle = Puzzle7()

currentPuzzle.RunMode = RU.REAL

print("Running Puzzle:", currentPuzzle.__class__.__name__)
start = time.perf_counter()
print(f"Part 1: {currentPuzzle.solve_part1()} in {(time.perf_counter() - start) * 1000:.3f}ms")

start = time.perf_counter()
print(f"Part 2: {currentPuzzle.solve_part2()} in {(time.perf_counter() - start) * 1000:.3f}ms")