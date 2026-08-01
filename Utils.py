# Not really usefull function here

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
    print(myHats[result_pseudoRandom])
    change_hat(myHats[result_pseudoRandom])
    if imIaWizzard:
        change_hat(Hats.Wizard_Hat)


def randomBaseOnPosition():
    return (get_pos_x() + get_pos_y()) % limiteHats
