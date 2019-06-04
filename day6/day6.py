# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

#
# def factorial(num):
#     """
#     求阶乘
#
#     :param num: 非负整数
#     :return: num的阶乘
#     """
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(factorial(m) // factorial(n) // factorial(m - n))

#
# def foo():
#     pass
#
#
# def bar():
#     pass
#
#
# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()
# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num
#
# def is_prime(num):
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
# if __name__ == '__main__':
#     num = int(input('请输入正整数: '))
#     if is_palindrome(num) and is_prime(num):
#         print('%d是回文素数' % num)


# def foo():
#     a = 200
#     print(a)  # 200
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100