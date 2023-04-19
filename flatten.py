def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    mytuple = ([1,"kot"], 3,(4, 5, [7, 8, 9]))
    myresult = flatten(mytuple)
    print(myresult)