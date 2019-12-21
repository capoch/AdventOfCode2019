from intcode import Intcode, Receiver
from game import Game

def main():
  sender = []
  receiver= Game("Game")
  inputLocation = 'input.txt'
  with open(inputLocation, 'r') as input:
      memory = [int(d) for d in input.read().split(",")]
  intcode = Intcode(memory, sender, [receiver])

  print(intcode.runProgram(False))

main()
