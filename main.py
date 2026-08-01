from Harverse import harvestProcess
from Utils import random_hat, showProgress


def walk_world(processFunction, showProgress=None, lastProgressShow=None) -> None:
    # Default walk function, i got mad without variable so I used the tuto
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            # faire un looping sur chaque case
            processFunction()
            lastProgressShow = showProgress(lastProgressShow)
            move(North)
        move(East)


def main():
    random_hat(False)
    lastProgressShow = get_time()
    while True:
        walk_world(harvestProcess, showProgress, lastProgressShow)


#        showProgress(lastProgressShow)


if __name__ == "__main__":
    main()
