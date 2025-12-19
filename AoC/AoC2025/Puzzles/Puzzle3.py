from puzzleBase import PuzzleBase

class Puzzle3(PuzzleBase):
    def get_test_data(test_data):
        return """987654321111111
811111111111119
234234234234278
818181911112111"""

    def solve_part1(self):
        lines = self.get_puzzle_input().splitlines()
        result = 0
        for line in lines:
            maxLeft = 0
            maxRight = 0
            split_index = 0
            for leftIndex in range(0, len(line) - 1):
                jolt = int(line[leftIndex])
                if  jolt > maxLeft:
                    maxLeft = jolt
                    split_index = leftIndex
            for rightindex in range(1, len(line) - split_index):
                jolt = int(line[rightindex * -1])
                if jolt > maxRight:
                    maxRight = jolt
            result += maxLeft * 10 + maxRight
        return str(result)



    def solve_part2(self):
        REQUIRED_BATTERIES = 12
        result = 0

        for line in self.get_puzzle_input().splitlines():
            line = [int(c) for c in line]
            line_pointer = 0
            line_result = 0
            for battery_count in range(12):
                max_jolt = 0
                for battery_pointer in range(line_pointer, len(line) - REQUIRED_BATTERIES + battery_count + 1):
                    if line[battery_pointer] > max_jolt:
                        max_jolt = line[battery_pointer]
                        line_pointer = battery_pointer + 1
                line_result = line_result * 10 + max_jolt
            print(line_result)
            result += line_result
        return result