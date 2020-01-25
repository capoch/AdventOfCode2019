# Solution approach:
# Transforming map of asteroids to a map in polar coordinates with the center on the Laser
# and the angle is measured from starting position of the laser clockwise (same way the laser turns)
# We then are looking for the 200th angle (counting by raising size starting with 0).
# Then find the polar point with said angle and smallest radius. Transform back to initial
# coordinate system


from geometry import Point, Vector, Map
import math

def main():
  asteroidMap = Map('input.txt').getAsteroids()
  polarMap = set()
  # cannonBase determined in first part of exercise
  cannonBase = Point(23,29)
  asteroidMap.remove(cannonBase)
  for asteroid in asteroidMap:
    newPoint = asteroid.changeCenterOfCoordinates(cannonBase[0], cannonBase[1]).flipYAxis().convertToPolar()
    polarMap.add(newPoint)
  asteroidDict = dict()
  for point in polarMap:
    if point[1] < 0:
      angle = point[1] + 2 * math.pi
    else:
      angle = point[1]
    if point[1] in asteroidDict.keys():
      asteroidDict[angle].append(point[0])
    else:
      asteroidDict[angle] = [point[0]]
  keyList = []
  for key in asteroidDict.keys():
    keyList.append(key)

  keyList.sort()
  print(keyList)
  targetAngle = keyList[199]
  distanceRange = asteroidDict[targetAngle]
  distanceRange.sort()
  targetDistance = distanceRange[0]

  result = Point(targetDistance, targetAngle).convertToCartesian().flipYAxis().changeCenterOfCoordinates(-cannonBase[0], -cannonBase[1])
  print(result[0], result[1])
  print("result: " + str(100*round(result[0])+round(result[1])))

main()
