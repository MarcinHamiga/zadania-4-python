def flatten(sequence):
    for item in sequence:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    mytuple = ([1,"kot"], 3,(4, 5, [7, 8, 9]))
    print("[", end="")
    for item in flatten(mytuple):
        print(item, end=" ")
    print("]", end="")
    print(list(flatten(mytuple)))