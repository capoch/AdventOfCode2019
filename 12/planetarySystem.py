from itertools import combinations
class System:
  _planets = set()
  _cyclesCompleted = 0

  def getCycle(self):
    return self._cyclesCompleted

  def __init__(self, setOfPlanets):
    self._planets = setOfPlanets

  def cycle(self):
    for planetPair in combinations(self._planets, 2):
      planetList = list(planetPair)
      planetList[0].cyclePosition(planetList[1])
      planetList[1].cyclePosition(planetList[0])
    #self.getPlanetInfo()
    for planet in self._planets:
      planet.applyVelocity()
    self._cyclesCompleted += 1

  def getTotalEnergy(self):
    totalEnergy = 0
    for planet in self._planets:
      totalEnergy += planet.getTotalEnergy()
    return totalEnergy

  def getPlanetInfo(self):
    for planet in self._planets:
      print(planet.getPosition(), planet.getVelocity())


class Planet:
  _position = list()
  _velocity = list()
  
  def __init__(self, positions, velocities):
    self._position = positions
    self._velocity = velocities
  
  def getPosition(self):
    return self._position

  def getVelocity(self):
    return self._velocity

  def cyclePosition(self, planet):
    for i in range(0,3):
      if planet.getPosition()[i] > self._position[i]:
        self._velocity[i] += 1
      elif planet.getPosition()[i] < self._position[i]:
        self._velocity[i] -= 1

  def applyVelocity(self):
    for i in range(0,3):
      self._position[i] += self._velocity[i]


  def getTotalEnergy(self):
    return (abs(self._position[0]) + abs(self._position[1]) + abs(self._position[2])) * (abs(self._velocity[0]) + abs(self._velocity[1]) + abs(self._velocity[2]))
