# is and not is- is called an identity operator that is used to check
# in and not in- membership operators

# task 1

list1 = [23, 56 , 79, 93, 2]
list2 = ["Sarah", "Adam", "Mariah", "Leo"]
list3 = [1, 23.4, 67, 67.67]

list4 = list2
print(list4 is list2)


# task 2

list = [23, 68, 90, 4, 5]
list2 = [32, 10, 3, 9, 56]

if 68 in list:
    print('The number 68 is in list')
else:
    print('The number 68 is not in list')