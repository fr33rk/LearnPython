from puzzleBase import PuzzleBase

class Puzzle2(PuzzleBase):
    def get_test_data(self):
        return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    def solve_part1(self) -> str:
        range_list = self.get_puzzle_input().split(",")
        result = 0
        for range_str in range_list:
            start, end = range_str.split("-")
            pattern = start[:len(start) // 2]

            if (pattern == ''):
                pattern = "0"

            while True:
                pattern_to_test = int(pattern * 2)
                if (pattern_to_test > int(end)):
                    break
                if (pattern_to_test >= int(start)):
                    result += int(pattern_to_test)
                pattern = str(int(pattern) + 1)
        
        return str(result)

    @staticmethod
    def is_invalid(n):
        s = str(n)
        length = len(s)
        if length < 2:
            return False
        for m in range(1, length // 2 + 1):
            if length % m == 0:
                k = length // m
                if k >= 2:
                    pattern = s[:m]
                    if s == pattern * k:
                        return True
        return False

    # With help of co
    def solve_part2(self) -> str:
        ranges = self.get_puzzle_input().split(",")
        result = 0
        for range_to_test in ranges:
            start, end = map(int, range_to_test.split("-"))
            for n in range(start, end + 1):
                if Puzzle2.is_invalid(n):
                    result += n

        return int(result)