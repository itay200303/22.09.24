
# start
my_list = list(range(10,101,10))

while True:
    num: int = int(input("Enter a num: "))
    if num == -999:
        break
    if num not in my_list:
        index = 0
        while index < len(my_list) and my_list[index] < num:
            index += 1
        my_list.insert(index, num)

print("the complete list:", my_list)

