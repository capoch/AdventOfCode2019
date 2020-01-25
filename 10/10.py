from geometry import Point, Vector, Map
from sys import argv

def main():
  if len(argv) < 2:
    map = Map('input.txt')
  else:
    map = Map(argv[1])
  maxAsteroidCount = 0
  maxAsteroid = None
  for centerPoint in map.getAsteroids():
    focusMap = map.asteroids.copy()
    targetCount = 0
    centerPointVector=Vector(centerPoint[0], centerPoint[1])
    focusMap.remove(centerPoint)
  
    while focusMap.__len__() > 0:
      targetSet = set()
      targetAsteroid = next(iter(focusMap))
      for asteroid in focusMap:

        if Vector(asteroid[0]-centerPoint[0], asteroid[1]-centerPoint[1]).direction(Vector(targetAsteroid[0]-centerPoint[0], targetAsteroid[1]-centerPoint[1])) > 0.999999999:
          targetSet.add(asteroid)
      focusMap -= targetSet
      targetCount +=1
    if targetCount > maxAsteroidCount:
      maxAsteroidCount = targetCount
      maxAsteroid = centerPoint
  print(maxAsteroidCount, maxAsteroid[0], maxAsteroid[1])

main()
