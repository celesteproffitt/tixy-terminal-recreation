# Import required components
from time import sleep
from os import name
from subprocess import run
import math

# Define variables
updateSpeed = 0.2
runtime = 20
screenSize = (8,8)
gradient = " -=oO0@"
equation = ""

# Define clear terminal function for moving to next frame
def clearTerminal():
    command = "cls" if name == "nt" else "clear"
    run([command], shell=True)

# Define main function
def main():
    time = 0

    # Runs for time listed in variables
    while time < runtime:

        # Creates the page by line
        page = ''
        for y in range(screenSize[1]):
            line = ''
            for x in range(screenSize[0]):

                # Define current (x,y) time, index, x, and y variables
                t = time
                i = y*screenSize[0]+x
                x = x
                y = y

                # Evaluates based on input equation, and fines appropriate gradient (0-1)
                tixy = abs(eval(equation))
                line += str(gradient[-1] if tixy>1 else gradient[round(tixy*(len(gradient)-1))])
            page+=line+'\n'

        # Clears screen and prints next frame with equation
        clearTerminal()
        print(page)
        print(equation)

        # Moves onto next loop based on loop length
        time+=updateSpeed
        sleep(updateSpeed)

# Asks for equation and runs main
equation = input("Enter desired equation: ") or "math.sin(t+y)"
main()
