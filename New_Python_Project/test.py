def first_func():
    name = input("What is your name? ")
    return name

def second_func(name):
    print(f"Hello, {name}")
    return

second_func(first_func())