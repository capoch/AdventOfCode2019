from geometry import Point, Vector, Map
import math

def main():
  asteroidMap = Map('input.txt').getAsteroids()
  polarMap = set()
  cannonBase = Point(23,29)
  for asteroid in asteroidMap:
    newPoint = asteroid.changeCenterOfCoordinates(cannonBase.x, cannonBase.y).flipYAxis().convertToPolar()
    polarMap.add(newPoint)
  asteroidDict = dict()
  for point in polarMap:
    if point.y in asteroidDict.keys():
      asteroidDict[point.y].append(point.x)
    else:
      asteroidDict[point.y] = [point.x]
  keyList = []
  for key in asteroidDict.keys():
    keyList.append(key)

  for key in keyList:
    if key < 0:
      key += 2 * math.pi

  keyList.sort()
  targetAngle = keyList[199]
  if targetAngle > math.pi:
    targetAngle -= 2 * math.pi
  distanceRange = asteroidDict[targetAngle]
  distanceRange.sort()
  targetDistance = distanceRange[0]

  print(targetDistance, targetAngle)
  print(targetDistance * math.sin(targetAngle), targetDistance * math.cos(targetAngle))

main()
