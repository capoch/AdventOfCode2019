import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "Point(" + str(self.x) + ", " + str(self.y) + ")"

  def distanceFrom(self, pointX):
    return math.sqrt(math.pow(pointX.y - self.y, 2) + math.pow(pointX.x - self.x, 2))

  def convertToPolar(self):
    return Point(math.sqrt(math.pow(self.x,2)+math.pow(self.y,2)),math.atan2(self.x,-1 * self.y))

  def changeCenterOfCoordinates(self, centerX, centerY):
    return Point(self.x-centerX, self.y-centerY)

  def flipYAxis(self):
    return Point(self.x, - self.y)

class Vector:
  def __init__(self,point):
    self.x = point.x
    self.y = point.y

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def product(self,vector):
    return self.x * vector.x + self.y * vector.y

  def abs(self):
    return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))

  def direction(self, vector):
    return self.product(vector) / (self.abs() * vector.abs())


class Map:
  asteroids = set()
  def __init__(self, inputLocation):
    with open(inputLocation, 'r') as input:
      lineCount = 0
      line = input.readline()
      while line:
        for i in range(0, len(line)):
          if line[i]=='#':
            self.asteroids.add(Point(i, lineCount))
        line = input.readline()
        lineCount += 1

  def getAsteroids(self):
    return self.asteroids
