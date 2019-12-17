from geometry import Point, Vector, Map

def main():
  map = Map('input.txt')
  maxAsteroidCount = 0
  maxAsteroid = None
  for centerPoint in map.getAsteroids():
    focusMap = map.asteroids.copy()
    targetCount = 0
    centerPointVector=Vector(centerPoint.x, centerPoint.y)
    focusMap.remove(centerPoint)
  
    while focusMap.__len__() > 0:
      targetSet = set()
      targetAsteroid = next(iter(focusMap))
      for asteroid in focusMap:

        if Vector(asteroid.x-centerPoint.x, asteroid.y-centerPoint.y).direction(Vector(targetAsteroid.x-centerPoint.x, targetAsteroid.y-centerPoint.y)) > 0.999999999:
          targetSet.add(asteroid)
      focusMap -= targetSet
      targetCount +=1
    if targetCount > maxAsteroidCount:
      maxAsteroidCount = targetCount
      maxAsteroid = centerPoint
  print(maxAsteroidCount, maxAsteroid.x, maxAsteroid.y)

main()
