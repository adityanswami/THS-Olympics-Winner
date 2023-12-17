def takeinput():
    inpu = []
    for i in range(8):
        inpu.append(int(input("Next value: ")))
    return inpu


def para(arr):
    numpar = 0
    if ((arr[3] - arr[1]) * (arr[6] - arr[4]) == (arr[2] - arr[0]) * (arr[7] - arr[5])):
        numpar += 1

    if ((arr[5] - arr[3]) * (arr[0] - arr[6]) == (arr[4] - arr[2]) * (arr[1] - arr[7])):
        numpar += 1

    return numpar


def perp(arr):
    numper = 0
    if ((arr[3] - arr[1]) * (arr[5] - arr[3]) == -((arr[2] - arr[0]) * (arr[4] - arr[2]))):
        numper += 1
    if ((arr[5] - arr[3]) * (arr[7] - arr[5]) == -((arr[4] - arr[2]) * (arr[6] - arr[4]))):
        numper += 1
    if ((arr[7] - arr[5]) * (arr[1] - arr[7]) == -((arr[6] - arr[4]) * (arr[0] - arr[6]))):
        numper += 1
    if ((arr[1] - arr[7]) * (arr[3] - arr[1]) == -((arr[0] - arr[6]) * (arr[2] - arr[0]))):
        numper += 1

    return numper


def checklengthequal(arr):
    if (((arr[0] - arr[2]) ** 2 + (arr[1] - arr[3]) ** 2) == ((arr[2] - arr[4]) ** 2 + (arr[3] - arr[5]) ** 2)):
        return True


def shape(arr):
    if (perp(arr) == 4 and para(arr) == 2):
        if checklengthequal(arr):
            return "square"
        else:
            return "rectangle"
    if (perp(arr) == 0 and para(arr) == 2):
        if checklengthequal(arr):
            return "rhombus"
        else:
            return "parallelogram"
    if (para(arr) == 1):
        return "trapezoid"
    return "quadrilateral"


for i in range(6):
    x = takeinput()
    print(shape(x))