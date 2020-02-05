import time
import math
 
class ResourceTreeNode:
  def __init__(self, recipe,leftovers):
    self.name = recipe[0][1]
    self.load = int(recipe[0][0])
    self.leftovers = leftovers
    self.multiplier = 1
    self.children = []
    self.parent = None

  def __str__(self):
    string = str(self.load) + " of " + self.name + " with a multiplier of " + str(self.multiplier) + ":"
    for child in self.children:
      childstring = str(child.load) + " of " + child.name +  ", "
      string += childstring

    return string

  def addChild(self, child):
    self.children.append(child)

  def hasChildren(self):
    return len(self.children) > 0

  def getIngredientLoad(self, recipe, ingredientName):
    for ingredient in recipe[1]:
      if ingredient[1] == ingredientName:
        return ingredient[0]
    else:
      return '0'

  def createTree(self, recipes, leftovers):
    currentNode = self
    ingredientList = recipes.get(currentNode.name)[1]
    for ingredient in ingredientList:
      ingredientRecipe = recipes.get(ingredient[1])
      if ingredientRecipe == None:
        ingredientRecipe = [ingredient,[]]
      child = ResourceTreeNode(ingredientRecipe, leftovers)
      currentNode.addChild(child)
      if child.name != "ORE":
        child.createTree(recipes, leftovers)
  
  def recalculate(self, recipes, leftovers):
    currentNode = self
    currentRecipe = recipes.get(currentNode.name)
    for child in self.children:
      targetAmount = currentNode.multiplier * int(currentNode.getIngredientLoad(currentRecipe, child.name))
      childLeftovers = leftovers.get(child.name)
      if childLeftovers > targetAmount:
        leftovers[child.name] = childLeftovers - targetAmount
        child.multiplier = 0
      else :
        child.multiplier = math.ceil((targetAmount - childLeftovers) / child.load)
        leftovers[child.name] = childLeftovers + child.multiplier * child.load - targetAmount
        
        leftovers[child.name] = childLeftovers + child.multiplier * child.load - targetAmount
      if child.name != "ORE":
        child.recalculate(recipes, leftovers)

  def printNodes(self):
    print(self)
    for node in self.children:
      if node.hasChildren():
        node.printNodes()
      else:
        print(node)

  def countElement(self, elementName): 
    elementCount = 0
    for child in self.children:
      if child.name == elementName:
        return child.load * child.multiplier
      else:
        elementCount += child.countElement(elementName)
    return elementCount
