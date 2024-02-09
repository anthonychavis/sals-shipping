class NegativeWeightError(Exception):
    '''Exception for negative weight values'''
    def __init__(self, weight: int | float) -> None: self.weight = weight
    def __str__(self) -> str: return f'{self.__class__.__name__}: You entered "{self.weight}", but the minimum allowed weight is 0 lbs.'
class InputLengthError(Exception):
    '''Exception for input exceeding allowed length'''
    def __init__(self, weight: int | float) -> None: self.weight = weight
    def __str__(self) -> str: return f'{self.__class__.__name__}: You entered "{self.weight}" which exceeds the allowed 10 number of digits.'