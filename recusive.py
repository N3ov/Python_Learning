def fav(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fav(n - 1) + fav(n - 2)



# print(fav(20))

# print(fav(10))

def _fav(m):

    a, b = 0, 1
    for i in range(m):
        a, b = b, a+b
    return a



# print(_fav(10))


