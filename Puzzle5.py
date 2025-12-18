test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def part_one(puzzle_input: str) -> str:
    puzzle_parts = puzzle_input.split("\n\n")
    ranges = [tuple(map(int, line.split('-', 1))) for line in puzzle_parts[0].split('\n') if line.strip()]
    ranges.sort()
    values_to_test =[int, line) for line in puzzle_parts[1].split('\n') if line.strip()]
    for value_to_test in values_to_test:
        for range in ranges:
            if value_to_test < range[0]:
                continue



part_one(test_input)
