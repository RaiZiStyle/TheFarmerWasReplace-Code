from Harverse import USER_NEEDS

# Not really usefull function here
PROGRESS_SHOW_TIME = 30  # Seconds
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


def showProgress(last_show: float, debug=False) -> float:
    # Print progress for each need. Returns updated timestamp.
    now = get_time()
    if now - last_show < PROGRESS_SHOW_TIME and not debug:
        return last_show

    time_str = seconds_to_dhms(now)
    separator = "+" + "------------------------------" + "+"

    print(separator)
    print("| [" + time_str + "] Progress Report")
    print(separator)

    for need in USER_NEEDS:
        current = num_items(need["NAME"])
        wanted  = need["WANTED"]
        percent = (current * 100) // wanted

        bar_filled = percent // 10
        bar = "[" + repeat_char("#", bar_filled) + repeat_char(".", 10 - bar_filled) + "]"

        line = (
            "| "
            + pad_right(need["TEXT"], 15)
            + bar
            + " "
            + pad_left(current, 4)
            + " / "
            + pad_left(wanted, 4)
            + " ("
            + pad_left(percent, 3)
            + "%)"
        )
        print(line)

    print(separator)
    return now

def repeat_char(char, count):
    result = ""
    for _ in range(count):
        result = result + char
    return result

def pad_left(value, width):
    s = str(value)
    return repeat_char(" ",(width - len(s))) + s

def pad_right(value, width):
    s = str(value)
    return s + repeat_char(" ",  (width - len(s)))

def random_elem(list):
    index = random() * len(list) // 1
    return list[index]


def seconds_to_dhms(seconds: float) -> str:
    d = seconds // 86400
    seconds = seconds % 86400
    h = seconds // 3600
    seconds = seconds % 3600
    m = seconds // 60
    s = seconds % 60
    rc = str(d) + "D" + str(h) + "H" + str(m) + "m" + str(s) + "s"
    return rc


if __name__ == "__main__":
    lastProgressShow = get_time()
    while True:
        lastProgressShow = showProgress(lastProgressShow, True)
