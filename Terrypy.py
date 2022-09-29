#Imports
import random
r = random.SystemRandom()
from colorama import init, Fore, Back, Style

#header 

def functionsnew():
    functions = '[1]Dice\n'
    print('Welcome, Im Terry nice to Meet You. Here are the Options\n')
    print(functions)
    input1 = input('Please choose something!\n')
    
    #Decision with if statement
    if input1 == 1:
        print('Please choose a differend number')
    else:
        dice()
        

def dice():
    min = int(input('Ah you chose the Dice, nice! So please choose a min number\n'))
    max = int(input('Input a max number\n'))
    randomnr = r.randint(min,max)
    print('Your number is:\n')
    print(randomnr)
    return functionsnew()

functionsnew()
    




    
  
    
