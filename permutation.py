import itertools


def perm(j, n):
    _list = [i for i in range(j)]
    # lista = random.shuffle(_list)
    perm = itertools.permutations(_list, n)
    print(list(perm))



def comb(j, n):

    _list = [i for i in range(j)]
    comb = itertools.combinations(_list, n)
    print(list(comb))



# perm(10, 2)
# comb(10, 2)

