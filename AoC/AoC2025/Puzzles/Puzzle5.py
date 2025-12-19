from puzzleBase import PuzzleBase

class Puzzle5(PuzzleBase):

    def get_test_data(test_data):
        return """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    def solve_part1(self):
        parts = self.get_puzzle_input().strip().split('\n\n')
        ranges = [tuple(map(int, line.split('-'))) for line in parts[0].split('\n')]
        ranges.sort()
        ingredient_ids = list(map(int, parts[1].split('\n')))
        fresh = 0
        for ingredient_id in ingredient_ids:
            for range in ranges:
                if ingredient_id < range[0]:
                    pass
                elif ingredient_id >= range[0] and ingredient_id <= range[1]:
                    fresh += 1
                    break
        return str(fresh)

    def solve_part2(self):
        parts = self.get_puzzle_input().strip().split('\n\n')
        ranges = [tuple(map(int, line.split('-'))) for line in parts[0].split('\n')]
        ranges.sort()
        fresh = 0
        previous = None
        for range in ranges:
            start = range[0]

            if previous != None and previous >= range[0]:
                start = previous + 1

            if start > range[1]:
                print(f'{range[0]}-{range[1]}: Skipped')
                continue

            new_elements = range[1] - start + 1
            if new_elements <= 0:
                continue
            print(f'{range[0]}-{range[1]}:{start}-{range[1]} = {new_elements}')
            fresh += range[1] - start + 1
        

            previous = range[1]

        # too low:  334555857184077
        # too high: 344486348901808
        # too high: 344486348901792

        return str(fresh)