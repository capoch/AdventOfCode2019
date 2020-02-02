from resourceTree import ResourceTreeNode
import time

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
  print(upperBound)
  counter = 0
  print("before while loop")
  while getOreNeededForFuel(upperBound, root, recipes, leftovers) < oreStored:
    print("in while loop")
    lowerBound = upperBound

    upperBound = 10*lowerBound
    print("New upperbound = " + str(upperBound))

  print("upperbound determined to be " + str(upperBound))

  while lowerBound < upperBound - 1:
    mid = (lowerBound + upperBound) // 2
    ore = getOreNeededForFuel(mid, recipes, leftovers)
    if counter % 5 == 0:
      print("low = " + str(lowerBound))
      print("high= " + str(upperBound))
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

def loadInput(inputLocation):
  recipes = dict()
  leftovers = dict()
  with open(inputLocation, 'r') as input:
    for line in input.read().splitlines():
      segments = line.split(" => ")
      compositeTargetIngredient = segments[1]
      targetIngredient = compositeTargetIngredient.split(" ")
      targetIngredientName = targetIngredient[1]
      targetIngredientAmount = int(targetIngredient[0])
      recipe = list()
      recipe.append(targetIngredient)
      ingredients = list()
      for compositeIngredient in segments[0].split(", "):
        ingredient = compositeIngredient.split(" ")
        leftovers[ingredient[1]] = 0
        ingredients.append(ingredient)
      recipe.append(ingredients)
      recipes[targetIngredient[1]] = recipe
  return (recipes, leftovers)

main()
