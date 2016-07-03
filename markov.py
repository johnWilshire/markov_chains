from graph import Graph
import re

chain = Graph()

f = open('news.txt')

for line in f.readlines():
    line = line.rstrip()
    line = re.sub("[^\w\s]","", line)
    words = re.split(' +', line.lower())
    for i in range(len(words) - 1):
        chain.add(words[i], words[i + 1])

#chain.print_nodes()

start = chain.random_choice()
sentence = []
sentence.append(start.contents.title())
for i in range(10):
    next_str = start.next()
    if next_str not in chain.nodes.keys():
        break
    sentence.append(next_str),
    start = chain.nodes[next_str]

print " ".join(sentence) + "."


