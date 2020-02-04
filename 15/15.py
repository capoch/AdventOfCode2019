from intcode import Intcode, Receiver

def main():
    fileLocation = 'input.txt'
    with open(fileLocation, 'r') as input:
        memory = [int(d) for d in input.read().split(',')]
        #memory = [109, 1, 203, 2, 204, 2, 99] 
        print(memory)
    intcode = Intcode(memory, None, [])

    print(intcode.runProgram(True))
    print(memory[1008])



main()
