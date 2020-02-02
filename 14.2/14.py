from recipe import Recipe, Material

def main():
  inputLocation = 'input.txt'
  data = loadInput(inputLocation)
  recipes = data[0]
  leftovers = data[1]
  print(recipes)
  print(leftovers)
  leftovers = dict()
  #print(root.getOres())

def loadInput(inputLocation):
  recipes = list()
  leftovers = dict()
  with open(inputLocation, 'r') as input:
    for line in input.read().splitlines():
      print(line)
      segments = line.split(" => ")
      output = Material(segments[1][0], segments[1][1])
      inputs = list()
      print(segments[0])
      for inputMaterial in segments[1].split(", "):
        inputs.append(Material(inputMaterial[0], inputMaterial[1]))      
      recipe = Recipe(output, inputs)
      leftovers[recipe.output.getName()] = 0
      recipes.append(recipe)
  return (recipes, leftovers)

main()
