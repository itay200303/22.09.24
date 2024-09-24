# start

my_list : list [int] = []
for i in range(1, 101):
    my_list.append(i)

print('my_list[0] -->', my_list[0])
print('my_list[-1] -->', my_list[-1])
print('my_list[: len(my_list)] -->', my_list[: len(my_list)])
print('my_list[3 - 12]-->', my_list[2:12])
print('my_list[80 - 100]-->', my_list[-21:100])
print('my_list[0 - 17]-->', my_list[0:17])
print('my_list[100, 99, 98 ...] -->', my_list[::-1])
print('my_list[zugi]-->', my_list[1::2])
print('my_list[%3]-->', my_list[2:100:3])
print('my_list[%7]-->', my_list[6:100:7])
print('my_list[+10]-->', my_list[9:100:10])
print('my_list[99 - 66]-->', my_list[98:64:-3])

my_list.insert(49, 999)
print(my_list)

my_list.pop(-1)
print(my_list)

# end