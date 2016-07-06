from graph import Graph
import re
import argparse

chain = Graph()

parser = argparse.ArgumentParser(
    description = 'Generates a sentence')
parser.add_argument('--filename', type=str,
    help='The corpus to generate a sentence from.')
parser.add_argument('--length', type=int, default=15,
    help='The max length of the generated sentence.')

args = parser.parse_args()


f = open(args.filename)

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

for i in range(args.length - 1):
    next_str = start.next()
    if next_str not in chain.nodes.keys():
        break
    sentence.append(next_str),
    start = chain.nodes[next_str]

print " ".join(sentence) + "."


