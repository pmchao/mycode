#my_list = [1, 2, 3,1, 0,4, 5, 0]
my_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to rearrange the list
#processed_list = [0 for i in my_list if i == 0] + [i for i in my_list if i not in [0, 1]] + [1 for i in my_list if i == 1]
#processed_list = [0 for i in my_list if i == 0]+ [i for i in my_list if i not in [0, 1]]
#print(processed_list)
divided_by_2_if_even = [x / 2 if x % 2 == 0 else x for x in my_list2]





print(divided_by_2_if_even)