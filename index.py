# Copyright 2019. Anas Abu Farraj
# Learning Python


class Egg:
    # Initial Constructors
    def __init__(self, kind="Fried"):
        self.kind = kind

    def what_kind(self):
        return self.kind


def main():
    fried = Egg()  # Use default value "Fried"
    scrambled = Egg("Scrambled")
    print(fried.what_kind())
    print(scrambled.what_kind())


if __name__ == "__main__":
    main()


# TODO: Study this example
class Door:
    def open(self):
        print("Hello stranger")


def knock_door():
    a_door = Door()
    Door.open(a_door)


knock_door()
