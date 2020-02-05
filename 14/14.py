from resourceTree import ResourceTreeNode
from shared import loadInput

def main():
  oreStored = 1000000000000
  inputLocation = 'input_final.txt'
  data = loadInput(inputLocation)
  recipes = data[0]
  leftovers = data[1]
  rootRecipe = recipes.get("FUEL")
  root = ResourceTreeNode(rootRecipe, leftovers)
  root.createTree(recipes, leftovers)
  oreForOneFuel = getOreNeededForFuel(1, root, recipes, leftovers)
  print("Ore for 1 FUEL = " + str(oreForOneFuel))

  lowerBound = oreStored // oreForOneFuel
  upperBound = 10 * lowerBound

  while getOreNeededForFuel(upperBound, root, recipes, leftovers) < oreStored:
    lowerBound = upperBound

    upperBound = 10*lowerBound


  while lowerBound < upperBound - 1:
    mid = (lowerBound + upperBound) // 2
    ore = getOreNeededForFuel(mid, root, recipes, leftovers)
    if ore < oreStored:
      lowerBound = mid
    elif ore > oreStored:
      upperBound = mid
    else:
      break

  print("10e12 ORE can produce " + str(mid - 1) + " FUEL")

def getOreNeededForFuel(fuelAmount, root, recipes, leftovers):
    root.multiplier = fuelAmount
    for key in leftovers.keys():
      leftovers[key] = 0
    root.recalculate(recipes, leftovers)
    return root.countElement("ORE")

main()
