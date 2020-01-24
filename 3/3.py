from math import sqrt, pow

def getInput():
  fileLocation = 'input.txt'
  inputTuple = list()
  with open(fileLocation, 'r') as input:
    for path in input:
      directions = list()
      for direction in path.split(','):
        directions.append(direction)
      inputTuple.append(directions)
  return inputTuple

def parseDirectionsToList(startingPoint, directionList):
  points = list()
  points.append(startingPoint)
  for i in range(len(directionList)):
    points.extend(calculatePointsFromDirection(points[-1], directionList[i]))
  return points

def calculatePointsFromDirection(currentPoint, direction):
  listOfPoints = list()
  directionIndicator = direction[0:1]
  pointRange = int(direction[1:])
  if directionIndicator == 'L':
    for i in range(1,pointRange+1):
      listOfPoints.append((currentPoint[0] - i, currentPoint[1]))
  elif directionIndicator == 'R':
    for i in range(1,pointRange+1):
      listOfPoints.append((currentPoint[0] + i, currentPoint[1]))
  elif directionIndicator == 'D':
    for i in range(1,pointRange+1):
      listOfPoints.append((currentPoint[0], currentPoint[1] - i))
  elif directionIndicator == 'U':
    for i in range(1,pointRange+1):
      listOfPoints.append((currentPoint[0], currentPoint[1] + i))
  return listOfPoints

def main():
  directions = getInput()
  distancesOfKnots = list()
  manhattenOfKnots = list()
  startingPoint = (0,0)
  pointsA = parseDirectionsToList(startingPoint, directions[0])
  setA = set(pointsA)
  pointsB = parseDirectionsToList(startingPoint, directions[1])
  setB = set(pointsB)
  intersection = set.intersection(setA,setB)
  for knot in intersection:
    distancesOfKnots.append(pointsA.index(knot)+pointsB.index(knot))
    manhattenOfKnots.append(sqrt(pow(knot[0],2)) + sqrt(pow(knot[1],2)))
  distancesOfKnots.sort()
  manhattenOfKnots.sort()
  print("3.1: " + str(manhattenOfKnots[1]))
  print("3.2: " + str(distancesOfKnots[1]))

main()
