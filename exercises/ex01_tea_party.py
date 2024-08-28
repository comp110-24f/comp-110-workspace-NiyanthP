"""Planning a cozy tea party excercise"""

__author__ = "730737669"


def main_planner(guests: int) -> None:
    """Puts everything together with function calls"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print(
        "{}{}".format("Cost: $", cost(tea_bags(people=guests), treats(people=guests)))
    )


def tea_bags(people: int) -> int:
    """Returns number of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns total cost of treats and tea"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    """Gets input from user and makes main_planner function call"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
