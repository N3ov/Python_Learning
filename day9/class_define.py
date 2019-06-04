class Test:

    def __init__(self, foo):
        self.__foo = foo #hello

    def __bar(self):
        print(self.__foo) #hello
        print('__bar') #__bar


def main():
    test = Test('hello')
    test._Test__bar() #直接呼叫Test __bar 
    print(test._Test__foo)


if __name__ == "__main__":
    main()