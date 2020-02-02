from resourceTree import ResourceTreeNode
from shared import loadInput

def main():
  inputLocation = 'input_final.txt'
  data = loadInput(inputLocation)
  recipes = data[0]
  leftovers = data[1]
  rootRecipe = recipes.get("FUEL")
  root = ResourceTreeNode(rootRecipe, leftovers)
  root.createTree(recipes, leftovers)
  root.recalculate(recipes, leftovers)
  print("Total amount of ORE needed: " + str(root.countElement("ORE")))

main()
