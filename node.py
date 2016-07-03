import random

class Node:
    def __init__(self, contents):
        self.neighbours = {}
        self.total = 0
        self.contents = contents


    def inc(self, neighbour):
        self.total += 1

        if neighbour in self.neighbours:
            self.neighbours[neighbour] += 1
        else:
            self.neighbours[neighbour] = 1

    def to_string(self):
        output = ""
        for node in self.neighbours:
            output += self.contents + " -" + str(
                float(self.neighbours[node])/self.total) + "-> " + node + "\n"
        return output

    def next(self):
        urn = random.uniform(0, 1)
        total = 0
        for node in self.neighbours:
            total = total + float(self.neighbours[node])/self.total
            if urn < total:
                return node

