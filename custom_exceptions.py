class NegativeWeightError(Exception):
    '''Exception for negative weight values'''
    def __init__(self, weight: int | float) -> None:
        self.weight = weight
    def __str__(self) -> str:
        return f'You entered {self.weight}, but the minimum allowed weight is 0 lbs.'