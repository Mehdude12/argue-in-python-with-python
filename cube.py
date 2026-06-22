def cube(sides):
    return sides * sides * sides


def evility(evillness):
    if evillness % 3 == 0:
        return cube(evillness)
    else:
        return False


print(evility(6))
print(evility(2222222222))
