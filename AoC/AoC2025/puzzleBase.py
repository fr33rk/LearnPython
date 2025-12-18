from abc import abstractclassmethod, abstractmethod
from enum import Enum, auto

class RunMode(Enum):
    TEST = auto()
    REAL = auto()

class PuzzleBase:
    
    @abstractmethod
    def get_test_data(test_data: str):
       raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def solve_part1(self) -> str:
        raise NotImplementedError("This method should be overridden by subclasses.")

    @abstractmethod
    def solve_part2(self) -> str:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def get_puzzle_input(self) -> str:
        if self.RunMode == RunMode.TEST:
            return self.get_test_data()
        elif self.RunMode == RunMode.REAL:

            with open (f".\Inputs\{self.__class__.__name__}.input", "r") as f:
                return f.read()

    RunMode: RunMode