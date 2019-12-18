from resourceTree import ResourceTreeNode, ResourceTree

def main():
  inputLocation = 'input.txt'
  ingredientList = loadInput(inputLocation)
  for ingredient in ingredientList:
    print(ingredient)
  completeRecipe = ResourceTree(ingredientList, "FUEL", 1)

def loadInput(inputLocation):
  ingredientList = []
  with open(inputLocation, 'r') as input:
    for line in input.read().splitlines():
      segments = line.split(" => ")
      compositeTargetIngredient = segments[1]
      targetIngredient = compositeTargetIngredient.split(" ")
      recipe = ResourceTreeNode(1, targetIngredient[1])
      for compositeIngredient in segments[0].split(", "):
        ingredient = compositeIngredient.split(" ")
        recipe.addChild(ResourceTreeNode(int(ingredient[0])/int(targetIngredient[0]), ingredient[1]))
      ingredientList.append(recipe)

  return ingredientList





main()
