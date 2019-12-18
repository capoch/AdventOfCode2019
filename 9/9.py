from intcode import Intcode

def main():
    fileLocation = 'input.txt'
    with open(fileLocation, 'r') as input:
        memory = [int(d) for d in input.read().split(',')]
        #memory = [109, 1, 203, 2, 204, 2, 99] 
        print(memory)
    intcode = Intcode(memory)

    print(intcode.runProgram([1], False))
    print(memory[1008])






main()
