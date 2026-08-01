def plantHay(water=False, fertilizer=False) -> None:
    plant(Entities.Grass)


def plantCarrot(water=False, fertilizer=False) -> bool:
    # Plant carrot, if can't, plant tree or grass.
    rc = False
    # Limite to plant carrot
    if num_items(Items.Wood) >= 100 and num_items(Items.Hay) >= 100:
        if get_entity_type() == Entities.Grass:
            harvest()
        if not get_ground_type() == Grounds.Soil:
            till()
        errorPlant = plant(Entities.Carrot)
        if not errorPlant:
            print("here")
        else:
            rc = True
        return rc
    else:
        if num_items(Items.Wood) <= 100:
            plantTree()
        elif num_items(Items.Hay) <= 100:
            plant(Entities.Grass)

        return rc


def plantTree(water=False, fertilizer=False) -> None:
    # Plant Tree, if can't, plant bush.
    rc = False

    # Get current coordinates
    x = get_pos_x()  # Current column (0, 1, 2, etc.)
    y = get_pos_y()  # Current row (0, 1, 2, etc.)

    # Checkerboard logic: Plant trees on "black squares", bushes on "white squares"
    # This ensures no two trees are adjacent (trees need space to grow)
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
        # "Black squares" - plant trees
        if not plant(Entities.Tree):
            rc = False

        waterAndFertilizer(water, fertilizer)

    else:
        # "White squares" - plant bushes
        plant(Entities.Bush)


def plantPumpkin(water=False, fertilizer=False) -> None:
    # Plant Pumpkin, if can't, plant Carrot.
    if not get_ground_type() == Grounds.Soil:
        till()
    if num_items(Items.Carrot) >= 10:
        plant(Entities.Pumpkin)
        waterAndFertilizer(water, fertilizer)
    else:
        plantCarrot(True, True)


def waterAndFertilizer(water=False, fertilizer=False) -> None:
    if num_items(Items.Water) >= 1 and water and get_water() <= 0.75:
        use_item(Items.Water)
    if num_items(Items.Fertilizer) >= 1 and fertilizer:
        use_item(Items.Fertilizer)


if __name__ == "__main__":
    clear()
    plantSomething()  # type: ignore
