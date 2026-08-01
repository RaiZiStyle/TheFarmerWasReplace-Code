from Harverse import USER_NEEDS

# Not really usefull function here
PROGRESS_SHOW_TIME = 60 # Seconds
lastProgressShow = get_time()
myHats = [
    Hats.Carrot_Hat,
    Hats.Green_Hat,
    Hats.Traffic_Cone,
    Hats.Wizard_Hat,
    Hats.Tree_Hat,
    Hats.Straw_Hat,
]
limiteHats = len(myHats)


def random_hat(imIaWizzard=False):
    result_pseudoRandom = randomBaseOnPosition()
    change_hat(myHats[result_pseudoRandom])
    if imIaWizzard:
        change_hat(Hats.Wizard_Hat)


def randomBaseOnPosition():
    return (get_pos_x() + get_pos_y()) % limiteHats


def showProgress(last_show: float) -> float:
    # Print progress for each need. Returns updated timestamp.
    now = get_time()
    if now - last_show < PROGRESS_SHOW_TIME:
        return last_show
    
    need = random_elem(USER_NEEDS) 
    currentProgress = num_items(need['NAME']) / need['WANTED']
    currentItem = need["TEXT"]
    currentTime = get_time()
#            test = get_entity_type(need["NAME"])
    print("Items :" + str(currentItem) + ",Progress :" + str(currentProgress))
    quick_print("["+str(currentItem) + "] - " + "Items :" + str(currentItem) + ",Progress :" + str(currentProgress))
    return now

def random_elem(list):
    index = random() * len(list) // 1
    return list[index]

if __name__ == "__main__":
    lastProgressShow = get_time()
    while True:
        lastProgressShow = showProgress(lastProgressShow)