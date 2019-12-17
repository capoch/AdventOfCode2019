from planetarySystem import *

def main():
  planets = set()
  planets.add(Planet([-7,-1,6],[0,0,0]))  
  planets.add(Planet([6,-9,-9],[0,0,0]))  
  planets.add(Planet([-12,2,-7],[0,0,0]))  
  planets.add(Planet([4,-17,-12],[0,0,0]))  
  
  system = System(planets)
  for i in range(0,1000):
    system.cycle()

  print(system.getCycle())
  print(system.getTotalEnergy())

main()
