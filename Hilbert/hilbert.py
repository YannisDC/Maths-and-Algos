import numpy as np

# up becomes down, left becomes right
def f(x):
    if x.shape:
        return array_map(x)
    else:
        if x == 0:
            return 1
        elif x== 1:
            return 0
        elif x== 2:
            return 3
        else:
            return 2

def array_map(x):
    return np.array(list(map(f, x)))

def hilbertCurve(order):
    if order == 1:
        return np.array([[2, 3], [1, 4]])
    else:
        lowerOrder = hilbertCurve(order-1)
        leftup = lowerOrder + np.amax(lowerOrder)
        leftdown = np.rot90(lowerOrder.transpose(), k=2, axes=(0, 1))

        rightup = lowerOrder + np.amax(leftup)
        rightdown = lowerOrder.transpose() + np.amax(rightup)

        concatLeft = np.concatenate((leftup, leftdown), axis=0)
        concatRight = np.concatenate((rightup, rightdown), axis=0)
        concat = np.concatenate((concatLeft, concatRight), axis=1)
        return concat

def directionCurve(order):
    if order == 1:
        return np.array([[3, 2], [1, 3]])
    else:
        lowerOrder = directionCurve(order-1)
        leftup = np.fmod(lowerOrder,4)
        leftdown = np.rot90(np.fmod(np.add(lowerOrder, 2), 4), k=2, axes=(0, 1)).transpose()

        rightup = np.fmod(lowerOrder,4)
        rightdown = np.fmod(array_map(lowerOrder).transpose(),4)

        concatLeft = np.concatenate((leftup, leftdown), axis=0)
        concatRight = np.concatenate((rightup, rightdown), axis=0)
        concat = np.concatenate((concatLeft, concatRight), axis=1)
        modded = np.fmod(concat,4)

        dim = 2**order

        modded.itemset((int(dim/2), 0), 1)
        modded.itemset((int(dim/2 - 1), int(dim/2 - 1)), 3)
        modded.itemset((int(dim/2 - 1), int(dim - 1)), 2)

        return modded

def hilbertTransform(image, directionMatrix, rank, x, y):
    x = x
    y = y
    im = image
    ht = np.array([])

    for i in range(1, rank+1):
        direction = directionMatrix[x, y]
        ht = np.append(ht, [im[x, y]], axis=0)

        if direction == 1:
            x -= 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            y += 1
        else:
            y -= 1

    return ht
