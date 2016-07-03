from node import Node
import random

class Graph:
    def __init__(self):
        self.nodes = {}

    def add(self, a, b):
        if a in self.nodes:
            self.nodes[a].inc(b)
        else:
            self.nodes[a] = Node(a)
            self.nodes[a].inc(b)

    def contains(self, a):
        return a in self.nodes.keys()
    
    def print_nodes(self):
        for node in self.nodes:
            print self.nodes[node].to_string()

    def random_choice(self):
        index = (self.nodes.keys())[int(random.uniform(0, len(self.nodes)))]
        return self.nodes[index]


