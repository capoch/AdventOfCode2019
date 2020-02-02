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
