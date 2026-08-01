from Harverse import harvestProcess
from Utils import random_hat

def walk_world(processFunction):
    # Default walk function, i got mad without variable so I used the tuto
    while True: 
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                #faire un looping sur chaque case
                processFunction()
                move(North)
            move(East)

def main():
    random_hat(False)
    walk_world(harvestProcess)
    

if __name__ == "__main__": 
    main()
