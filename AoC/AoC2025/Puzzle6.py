from puzzleBase import PuzzleBase
import re

class Puzzle6(PuzzleBase):
    
    def get_puzzle_input(self):
        return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

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
        lines = self.get_puzzle_input().strip().splitlines()
        numbers_regex = re.compile(r'\d+')
        operators_regex = re.compile(r'[\+\*]')
        numbers = []
        answer = 0;
        for line in lines[0:-1]:
            numbers.append(numbers_regex.findall(line))
        
        operators = operators_regex.findall(lines[-1])

        return "hellup"
        #for problem in range(len(numbers[0])):

