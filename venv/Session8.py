# Whatever we write as python program will be executed by main thread
# main thread shall execute instruction in a sequence

# __name__ prints name of module
# print("__name__ is:",__name__) # main

import Session7D

print()

print("__name__ in Session8.py is:",__name__)

def main():

    a = 10
    b = [10, 20, 30, 40, 50]

    print(a)
    print(b)


if __name__ == "__main__":
    main()