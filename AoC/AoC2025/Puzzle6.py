from puzzleBase import PuzzleBase
import re

class Puzzle6(PuzzleBase):
    
    def get_puzzle_input(self):
        return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    def solve_part1(self) -> str:
        lines = self.get_puzzle_input().strip().splitlines()
        numbers_regex = re.compile(r'\d+')
        operators_regex = re.compile(r'[\+\*]')
        numbers = []
        answer = 0;
        for line in lines[0:-1]:
            numbers.append(numbers_regex.findall(line))
        
        operators = operators_regex.findall(lines[-1])

        for problem in range(len(numbers[0])):
            solution = int(numbers[0][problem])
            for element in range(1, len (numbers)):
                if (operators[problem] == '+'):
                    solution += int(numbers[element][problem])
                elif (operators[problem] == '*'):
                    solution *= int(numbers[element][problem])
                else:
                    raise ValueError("Unknown operator")
            answer += solution

        return answer

    def solve_part2(self) -> str:
        lines = self.get_puzzle_input().splitlines()

        # operator is the startindex
        start = 0
        operator_line = lines[-1]
        operator_line_len = len(operator_line)
        for index in range(operator_line_len):
            if index == operator_line_len-1 or operator_line[index+1] in ['+', '*']:
                if (index == operator_line_len-1):
                    index += 1

                matrix = [[c for c in line[start:index]] for line in lines[0:-1]]

                # Transpose using zip
                transposed = [list(row) for row in zip(*matrix)]
                print(transposed)
                start = index+1




        return "lekker busy"

