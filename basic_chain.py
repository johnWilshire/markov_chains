from graph import Graph

chain = Graph()

chain.add("a", "b")
chain.add("a", "b")
chain.add("a", "b")
chain.add("a", "d")
chain.add("a", "c")
chain.add("c", "d")
chain.add("a", "c")

chain.print_nodes()

print chain.random_choice().next()