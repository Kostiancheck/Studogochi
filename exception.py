class NegativeStatistic(Exception):
    def __init__(self, stat):
        self.stat = stat


class NegativeStatisticGrades(Exception):
    def __init__(self, stat):
        self.stat = stat

class BigNumException(Exception):
    def __init__(self, stat):
        self.stat = stat