import sys
sys.setrecursionlimit(9000000)

count = 0


def ack(m, n):
    global count

    if m == 0:
        count += 1
        return n + 1

    elif m > 0 and n == 0:
        count += 1
        return ack(m - 1, 1)

    else:
        count += 1
        return ack(m - 1, ack(m, n - 1))

print(ack(4, 2))
print(count)



# def A(m, n):
#     # print(s % ("A(%d,%d)" % (m, n)))
#     if m == 0:
#         return n + 1
#     if n == 0:
#         return A(m - 1, 1)
#     # n2 = A(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
#     return A(m - 1, A(m, n-1))
#
# print (A(2,2))

# def ackermann(m, n):
#     """computes the value of the Ackermann function for the input integers m and n.
#        the Ackermann function being:
#        A(m,n)=n+1               if m=0
#              =A(m-1,1)          if m>0 and n=1
#              =A(m-1,A(m,n-1)    if m>0 and n>0"""
#     if m == 0:
#         print(n+1)
#         return n+1
#     elif m > 0 and n==0:
#         print("ackermann(", m - 1, ",", 1, ")")                                          #just 2 chk intrmdt val. and no. of steps invlvd.can be dltd if necessary
#         return ackermann(m-1, 1)
#     elif m > 0 and n > 0:
#         print("Ackermann(", m-1, ",", "Ackermann(", m, ",", n-1, ")", ")")                  #just 2 chk intrmdt val. and no. of steps invlvd.can be dltd if necessary
#         return ackermann(m-1, ackermann(m, n-1))
#
#
# print(ackermann(2, 2))





