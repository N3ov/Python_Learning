a = 0
b = 1
for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')

'''
費波曼常數
'''

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


'''
水仙花辦數
'''