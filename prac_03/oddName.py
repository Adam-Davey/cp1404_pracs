"""Adam Davey"""


def main():
    name = get_name()
    print_parts(name, 3)


def print_parts(name, step=2):
    print(name[::step])


def get_name():
    name = input("what is your name?:")
    while name == "":
        print("invalid name")
        name = input("what is your name?:")
    return name


main()
