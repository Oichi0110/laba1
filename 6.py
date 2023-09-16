def isnit(s):
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


def array_int_float_number(array):
    for i in range(0, len(array)):
        if isnit(array[i]):
            array[i] = int(array[i])
        elif isfloat(array[i]):
            array[i] = float(array[i])
        else:
            print("Введите только целые или дробные числа")
            main()
    list_tuple_array(array)


def sequence_numbers_correct(sequence_numbers):
    sequence_numbers = sequence_numbers.replace(" ", "")
    sequence_numbers = sequence_numbers.split(",")
    i = 0
    while i < len(sequence_numbers):
        if sequence_numbers[i] == '' and i > 0:
            sequence_numbers.pop(i)
            i = i - 1
            continue
        elif sequence_numbers[i] == '' and i == 0:
            sequence_numbers.pop(i)
            continue
        i = i + 1
    array_int_float_number(sequence_numbers)


def list_tuple_array(array):
    print("Список - {}" .format(list(array)), "\nКортеж - {}" .format(tuple(array)))
    exit()


def main():
    sequence_number = input("Введите последовательность чисел(\",\"): ")
    sequence_numbers_correct(sequence_number)


if __name__ == "__main__":
    main()
