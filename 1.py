def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def conv(second):
    minutes = 0
    hours = 0
    days = 0
    minutes = second // 60
    if minutes > 60:
        hours = minutes // 60
        minutes = minutes - hours * 60
        second = second - minutes * 60 - hours * 60 * 60
        if hours > 24:
            days = hours // 24
            hours = hours - days * 24
            print(f'{days}:{hours}:{minutes}:{second}')
            main()
        else:
            print(f'{days}:{hours}:{minutes}:{second}')
            main()
    else:
        second = second - minutes * 60
        print(f'{days}:{hours}:{minutes}:{second}')
        main()


def main():
    print("0 - выход из программы")
    second = input("Second = ")
    if isint(second):
        second = int(second)
        if second < 0:
            print("Negative number")
            main()
        elif second > 0:
            conv(second)
        elif second == 0:
            exit()
    else:
        print("Error")
        main()


if __name__ == "__main__":
    main()
