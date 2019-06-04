def main():
    # f = None

    try:
        # f = open('致橡树.txt', 'r', encoding='utf-8')
        with open('code.txt', 'r', encoding = 'utf-8'):
            print(f.read())

    except FileNotFoundError:
        print('無法打開指定檔案')

    except LookupError:
        print('指定未知的code')

    except UnicodeDecodeError:
        print('讀取文件時解碼錯誤')
     
    # finally:
    #     if f:
    #         f.close

if __name__ == '__main__':
    main()