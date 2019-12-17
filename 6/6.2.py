def main():
  inputLocation = 'input.txt'
  
  totalOrbitCount = 0

  orbitList = dict()

  with open(inputLocation, 'r') as input:
    for inputLine in input.readlines():
      orbit = inputLine.strip().split(')')
      orbitList[orbit[1]] = orbit[0]
  planet1 = orbitList['YOU']
  planet2 = orbitList['SAN']  
  firstPlanetPath = getPath(planet1, orbitList)
  secondPlanetPath = getPath(planet2, orbitList)
  firstPlanetPath.reverse()
  secondPlanetPath.reverse()
  crossingPoint = findFirstIntersection(firstPlanetPath, secondPlanetPath)
  
  print len(firstPlanetPath) + len(secondPlanetPath) - 2 * crossingPoint

def getPath(planet, orbitList):
  path = list()
  
  while(orbitList[planet] != 'COM'):
    path.append(planet)
    planet = orbitList[planet]
  path.append('COM')
  return path

def findFirstIntersection(list1, list2):
  i = 0
  while (list1[i]==list2[i]):
    i += 1
  return i

main()
