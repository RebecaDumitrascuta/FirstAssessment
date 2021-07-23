my_initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("My initial list:", my_initial_list)

my_initial_list.sort()
print("My ascending list: ", my_initial_list)

my_initial_list.sort(reverse=True)
print("My descending list: ", my_initial_list)

my_even_list = my_initial_list[::2]
print("My even list:", my_even_list)

# am gasit si variantele de mai jos, pe care am vrut sa le incerc:
#    [ returned value; iteration; condition ]
even_list = [x for x in my_initial_list if x % 2 == 0]
print(even_list)
new_even_list = []
for x in my_initial_list:
    if x % 2 == 0:
        new_even_list.append(x)
print(new_even_list)

my_odd_list = my_initial_list[1::2]
print("My odd list:", my_odd_list)
odd_list = [x for x in my_initial_list if x % 2 != 0]
print(odd_list)
new_odd_list = []
for x in my_initial_list:
    if x % 2 != 0:
        new_odd_list.append(x)
print(new_odd_list)


multiple_of_three = my_initial_list[1::3]
print("My multiple of three list:", multiple_of_three)

