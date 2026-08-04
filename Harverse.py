from Plants import plantHay, plantCarrot, plantPumpkin, plantTree

WANTED_PUMPKIN = 512000
WANTED_WOOD = 154000
WANTED_CARROT = 128000
WANTED_HAY = 300000

WORLD_SIZE = get_world_size()
WORLD_HALF = WORLD_SIZE // 2


def harvestProcess() -> None:
    if can_harvest():
        harvest()
    if not plantProcess():
        while True:
            print("I'm borded, idk what do to")
            clear()
            do_a_flip()


USER_NEEDS = [
    {"NAME": Items.Pumpkin, "PRIO": 1, "WANTED": WANTED_PUMPKIN, "FUNCTION": plantPumpkin, "TEXT": "PUMPKIN"},
    {"NAME": Items.Wood, "PRIO": 2, "WANTED": WANTED_WOOD, "FUNCTION": plantTree, "TEXT": "WOOD"},
    {"NAME": Items.Carrot, "PRIO": 3, "WANTED": WANTED_CARROT, "FUNCTION": plantCarrot, "TEXT": "CARROT"},
    {"NAME": Items.Hay, "PRIO": 999, "WANTED": WANTED_HAY, "FUNCTION": plantHay, "TEXT": "HAY"},
]

IDLE_PRIO = 999

# TODO SUPPLY
SUPPLY = [
    {"ITEM": Items.Water, "PRIO": 1, "WANTED": 1, "FUNCTION": "", "NAME": "WATER"},
    {"ITEM": Items.Fertilizer, "PRIO": 1, "WANTED": 1, "FUNCTION": "", "NAME": "FERTILIZER"},
    {"ITEM": Items.Weird_Substance, "PRIO": 1, "WANTED": 20000, "FUNCTION": "", "NAME": "WEIRD_SUBSTANCE"},
]


def plantProcess() -> bool:
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

    companion = get_companion()
    xBefore, yBefore = get_pos_x(), get_pos_y()
    if companion != None:
        plant_type, (x, y) = companion
        for need in USER_NEEDS:
            if need["NAME"] == plant_type:
                # BUG: Doesn't work
                # get_companion() can return GRASS, but we don't have a plantGrass() function, so we need to check if the plant_type is in USER_NEEDS before calling the function.
                move_to(x, y)
                need["FUNCTION"](True, True)
                move_to(xBefore, yBefore)
        # print("Companion:", plant_type, "at", x, ",", y)
    return True


def move_to(x, y):
    x1 = get_pos_x()
    y1 = get_pos_y()
    x2, y2 = x, y

    dx = (x2 - x1 + WORLD_HALF) % WORLD_SIZE - WORLD_HALF
    dy = (y2 - y1 + WORLD_HALF) % WORLD_SIZE - WORLD_HALF

    if dx > 0:
        x_dir = East
    else:
        x_dir = West

    if dy > 0:
        y_dir = North
    else:
        y_dir = South

    adx = abs(dx)
    for i in range(adx):
        move(x_dir)

    ady = abs(dy)
    for i in range(ady):
        move(y_dir)
