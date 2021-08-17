class Route:

    id = int
    start = []
    end = []

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def toPrint(self):
        print(f'Start: {self.start} - End: {self.end}')
