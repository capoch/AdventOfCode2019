from intcode import Intcode
from robot import Robot

def main():
  data= [1]
  robot = Robot(data, "robo1")

  fileLocation = 'input.txt'
  with open(fileLocation, 'r') as input:
    program = [int(d) for d in input.read().split(',')]

  intcode = Intcode(program, data, [robot])
  registration = intcode.runProgram(False)

  print(registration)

  for i in range(0,-6,-1):
    line = []
    for j in range(0,41):
      if (j,i) in registration and registration[(j,i)]==1: 
        line.append('X')
      else:
        line.append(' ')
    print(line)




  print((1,0) in registration)
  print(registration[(1,0)])

main()
