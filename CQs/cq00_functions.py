"""My first CQ in COMP110!"""

__author__ = "730737669"


def mimic(message: str) -> str:
    """Returns the input string"""
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
