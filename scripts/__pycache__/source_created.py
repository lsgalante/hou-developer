import hou

network = hou.node(".")
node = kwargs['node']

solver = network.createNode("solver")

solver.setInput(0, node, 0)