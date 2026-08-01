from Plants import plantHay, plantCarrot, plantPumpkin, plantTree

WANTED_PUMPKIN = 10000
WANTED_WOOD = 54000
WANTED_CARROT = 3000
WANTED_HAY = 30000


def harvestProcess():
    if can_harvest():
        harvest()
    if not plantProcess():
        while True:
            print("I'm borded, idk what do to")
            clear()
            do_a_flip()


USER_NEEDS = [
    # {ITEM,PRIO, WANTED
    {"NAME": Items.Hay, "PRIO": 999, "WANTED": WANTED_HAY, "FUNCTION": plantHay},
    {"NAME": Items.Wood, "PRIO": 2, "WANTED": WANTED_WOOD, "FUNCTION": plantTree},
    {"NAME": Items.Carrot, "PRIO": 3, "WANTED": WANTED_CARROT, "FUNCTION": plantCarrot},
    {"NAME": Items.Pumpkin,"PRIO": 1,"WANTED": WANTED_PUMPKIN,"FUNCTION": plantPumpkin,},
    #    {"ITEM":Items.Power "PRIO":4,"WANTED":20000, "FUNCTION": plantCarrot},
]

IDLE_PRIO = 999

# TODO SUPPLY
SUPPLY = [
    {"ITEM": Items.Water, "PRIO": 1, "WANTED": 20000, "FUNCTION": ""},
    {"ITEM": Items.Fertilizer, "PRIO": 1, "WANTED": 20000, "FUNCTION": ""},
    {"ITEM": Items.Weird_Substance, "PRIO": 1, "WANTED": 20000, "FUNCTION": ""},
]


def plantProcess():
    selected = None
    bestPrio = 999999

    # Search the plant in USER_NEEDS
    for need in USER_NEEDS:
        # Vérifie si on manque de cet item
        if num_items(need["NAME"]) < need["WANTED"]:
            # Vérifie si c'est plus prioritaire
            if need["PRIO"] < bestPrio:
                selected = need
                bestPrio = need["PRIO"]

    # Exit if if PRIO is MAX and WANTED is obtain
    if selected == None:
        return False

    selected["FUNCTION"](True, True)

    return True
