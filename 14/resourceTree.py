class ResourceTreeNode:
  def __init__(self, load, name):
    self.name = name
    self.load = load
    self.children = []

  def __str__(self):
    return str(self.load) + " of " + self.name

  def addChild(self, child):
    self.children.append(child)

class ResourceTree:
  headNode = None
  def __init__(self, resourceList, headNodeName, multiplier):
    for sublist in resourceList:
      if sublist.name==headNodeName:
        self.headNode = sublist
        self.headNode.load *= multiplier
        #print("headnode " + str(self.headNode.load) + " " + self.headNode.name + "found")
    for child in self.headNode.children:
      if child.name != "ORE":
        #print("child: " + child.name + ", " + str(child.load))
        ResourceTree(resourceList, child.name, child.load)
      else:
        ResourceTreeNode(child.load / self.headNode.load, child.name)
        print(str(self.headNode.load * child.load) + " of ORE")
