from resourceTree import ResourceTreeNode
import time
from shared import loadInput

def main():
  oreStored = 1000000000000
  fuelProduced = 0
  treeCreationStartTime = time.time()
  inputLocation = 'input_final.txt'
  data = loadInput(inputLocation)
  recipes = data[0]
  leftovers = data[1]
  rootRecipe = recipes.get("FUEL")
  root = ResourceTreeNode(rootRecipe, leftovers)
  root.createTree(recipes, leftovers)
  print("--- Tree Creation Time in s %s ---" % (time.time() - treeCreationStartTime))
  print(str(getOreNeededForFuel(1, root, recipes, leftovers)))
  ## break to stop evaluating loop before getting tree recalculation right
  return 1

  lowerBound = oreStored // getOreNeededForFuel(1, root, recipes, leftovers)
  upperBound = 10 * lowerBound

  counter = 0
  while getOreNeededForFuel(upperBound, root, recipes, leftovers) < oreStored:
    lowerBound = upperBound

    upperBound = 10*lowerBound


  while lowerBound < upperBound - 1:
    mid = (lowerBound + upperBound) // 2
    ore = getOreNeededForFuel(mid, recipes, leftovers)
    if ore < oreStored:
      lowerBound = mid
    elif ore > oreStored:
      upperBound = mid
    else:
      break
  counter += 1

  print(mid)

def getOreNeededForFuel(fuelAmount, root, recipes, leftovers):
    fuelProduced = 0
    oreRequired = 0
    while(fuelProduced < fuelAmount):
      recalculationStartTime = time.time()
      root.recalculate(recipes, leftovers)
      print("--- Tree Recalculation time in  seconds %s ---" % (time.time() - recalculationStartTime))
      fuelProduced += 1
      oreRequired += root.countElement("ORE")
    return oreRequired

main()
