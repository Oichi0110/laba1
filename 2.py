import re
test_str = input("String = ")
beg_str = test_str.split()
size = len(beg_str)
print('str = \"{}\"' .format(test_str))
res_list = []
i = 0
while i < size:
    res = (re.sub('.', lambda x: r'%04X' % ord(x.group()), beg_str[i]))
    res_list.append(res)
    i += 1
max_word = max(beg_str, key=len)
res_list = " ".join(res_list)
print('Unicode str = \"{}\".' .format(res_list))
print('max word = \"{}\"' .format(max_word))
