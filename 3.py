def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def sum_pr_list(my_list):
    new_list = []
    size_beg_list = len(my_list)
    for i in range(0, size_beg_list):
        new_list.append(my_list[i]**3)
    sum = 0
    pr = 1
    for i in range(0, size_beg_list):
        sum += new_list[i]
        pr *= new_list[i]
    end_list = list(reversed(new_list))
    print("beg list = {}" .format(my_list), "\nnew_list = {}" .format(end_list), "\nSum = {}" .format(sum), "\nPr = {}" .format(pr))


def main():
    n = input("n = ")
    if isint(n):
        n = int(n)
        if n > 0:
            my_list = []
            i = 0
            while i < n:
                print('{} элемент' .format(i))
                x = input()
                if isint(x):
                    x = int(x)
                    my_list.append(x)
                    i += 1
                elif isfloat(x):
                    x = float(x)
                    my_list.append(x)
                    i += 1
            sum_pr_list(my_list)
        else:
            print("Отрицательно число, введите положительное")
            main()
    else:
        print("Error")
        main()


if __name__ == "__main__":
    main()
