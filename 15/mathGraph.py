from geometry import Point

class Node:
  def __init__(self, point, connections):
    self.point = point
    self.connections = connections

class mapGraph(dict):
  def __init__(self):
    self = dict()

  def addNode(self, currentNode, newNode):
    self[currentNode].append(newNode)

  def breadthFirstSearch(self, startingNode):
    for node in startingNode.connections:
      if node == '2':
        return node.point
      elif node == '#':
        remove(node)
      else:
        graph.addNode(node)
        breadthFirstSearch(node)
