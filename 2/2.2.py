def main():
  targetValue = 19690720
  memory = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]
  for noun in range(0,99):
    for verb in range(0,99): 
      opcodes = setState(memory, noun, verb)
      for i in range(0, len(opcodes), 4):
        if opcodes[i]==99:
          if opcodes[0]==targetValue:
            print 100 * noun + verb
          else:
            break
        elif opcodes[i]==1:
          opcodes[opcodes[i+3]]=opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]
        elif opcodes[i]==2:
          opcodes[opcodes[i+3]]=opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

def setState(memory, noun, verb):
  if(len(memory)<3):
    print "FUCK"
  result = list(memory)
  result[1] = noun
  result[2] = verb
  return result

main()
