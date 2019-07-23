

def divPrime(num):

    lt = []

    if num != 1:
        for i in range(2, int(num)):
            if num % i == 0:

                lt.append(i)

    if lt == []:
        print(num, "is Prime.")

    else:
        print(lt)


if __name__ == '__main__':
    divPrime(18)
