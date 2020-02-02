from resourceTree import ResourceTreeNode

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
