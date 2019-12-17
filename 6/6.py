def main():
  inputLocation = 'input.txt'
  
  totalOrbitCount = 0

  orbitList = dict()

  with open(inputLocation, 'r') as input:
    for inputLine in input.readlines():
      orbit = inputLine.strip().split(')')
      orbitList[orbit[1]] = orbit[0]
  
  for planet in orbitList.keys():
    totalOrbitCount += getTotalOrbitCount(planet, orbitList)

  print totalOrbitCount

def getTotalOrbitCount(planet, orbitList):
  count = 1
  while orbitList[planet] != 'COM':
    planet = orbitList[planet]
    count += 1
  return count
  


main()
