import time
#未指定路徑
#需在相同資料夾
def main():
    #一次性讀取文件內容
    with open('code132.txt', 'r', encoding= 'utf-8') as f:
        print(f.read())

    #透過 for - in loop 讀取
    with open('code132.txt', 'r', encoding= 'utf-8') as f:
        for line in f:
            print(line, end = '')
            time.sleep(0.5)

    print()

    #直接讀取文件到list
    with open('code132.txt') as f:
        lines = f.readlines()

    print(lines)


if __name__ == '__main__':
    main()