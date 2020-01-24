from intcode import Intcode
from robot import Robot

def main():
  data= [0]
  robot = Robot(data, "robo1")

  fileLocation = 'input.txt'
  with open(fileLocation, 'r') as input:
    program = [int(d) for d in input.read().split(',')]

  intcode = Intcode(program, data, [robot])
  print(intcode.runProgram(True))







main()
