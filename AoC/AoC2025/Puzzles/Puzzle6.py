from puzzleBase import PuzzleBase
from math import prod
import re

class Puzzle6(PuzzleBase):
    
    def get_test_data(self):
        return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    def solve_part1(self) -> str:
        lines = self.get_puzzle_input().strip().splitlines()
        numbers_regex = re.compile(r'\d+')
        operators_regex = re.compile(r'[\+\*]')
        numbers = []
        answer = 0
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

        return str(answer)

    @staticmethod
    def to_number(chars: list[str]) -> int:
        result = 0
        for c in chars:
            if c != ' ':
                result *= 10
                result += int(c)

        return result

    def solve_part2(self) -> str:
        lines = self.get_puzzle_input().splitlines()

        # We need to make 'blocks' of columns separated by operators. 
        # Then we transpose each block to get the numbers, perform the operation, and sum the results.

        # for convenience
        operator_line = lines[-1]
        operator_line_len = len(operator_line)

        # Initialize
        start = 0
        operator = operator_line[0]
        result = 0

        for index in range(operator_line_len):
            if index == operator_line_len-1 or operator_line[index+1] in ['+', '*']:
                
                # determine next_operator safely
                next_operator = operator_line[index+1] if index < operator_line_len-1 else None

                if (index == operator_line_len-1):
                    index += 1

                matrix = [[c for c in line[start:index]] for line in lines[0:-1]]

                # Transpose using zip
                transposed = [list(row) for row in zip(*matrix)]
                transposed_numbers = [Puzzle6.to_number(number) for number in transposed]

                solution = 0
                if operator == '+':
                    solution = sum(transposed_numbers)
                elif operator == '*':
                    solution = prod(transposed_numbers)

                result += solution
                start = index+1
                operator = next_operator

        return str(result)     