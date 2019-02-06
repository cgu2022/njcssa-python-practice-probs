    #######################################################################################
# 10.1
# Make an empty list and print it

list = []
print(list)

#######################################################################################
# 10.2
# Make a list holding the values 1, 2, 3, 4, 5 and then print the second and fifth item 
# using their index numbers. 

list = [1,2,3,4,5]
print(str(list[1]) + ' ' + str(list[4]))


#######################################################################################
# 10.3
# Use negative list indexes to access the last item in a list of [1, 2, 3, 4] and print
# the item.

list = [1,2,3,4]
print(str(list[-1]))

#######################################################################################
# 10.4
# Create a list and have it store 4 variables of 4 different types. Then print out the 
# list.

list = [True, 1, 5.3, 'Hello']
print(list)


#######################################################################################
# 10.5
# Create a list of lists. The outer list holds 3 inner lists that each hold 2 items. 
# The smaller lists can store anything you want. After you have made the list of lists, 
# print out each small list on a new line.

list = [[1, True], ['Hello', 2.5], [1, 2.4]]
for i in range(len(list)):
    print(list[i])

#######################################################################################
# 10.6
# Take the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and use list slicing to print a list
# that holds [3, 4, 5]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[2:5])

#######################################################################################
# 10.7
# Create a list and use the len() function to print out the length of the list.

list = [1,2,'Hello',True,5.3]
print(len(list))

#######################################################################################
# 10.8
# Create a list. Print it. Then change at least 2 values inside it. Print out the
# changed list.

list = [1,2,3,4,5]
print(list)
list[0] = 2
list[1] = 3
print(list)

#######################################################################################
# 10.9
# Create a list. Use a for loop to loop through the list using a counter variable and
# print each item.

list = [10,20,30,40,50]
for i in range(len(list)):
    print(list[i])

#######################################################################################
# 10.10
# Create a list. Use a for loop to loop through the list using the "in" keyword and 
# print each item.

list = [10,20,30,40,50]
for i in list:
    print(i)

#######################################################################################
# 10.11
# Create a list consisting of integers. Use a for loop to loop through the list and add
# 1 to all the items. Then print out the changed list.

list = [1,2,3,4,5]
for i in range(len(list)):
    list[i] += 1
print(list)

#######################################################################################
# 10.12
# Create 2 lists. Take the lists and create 1 bigger list using both lists. Print the 
# bigger list.

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1 += list2
print(list1)

#######################################################################################
# 10.13
# Create a list of 5 items. Remove 2 items from the end and print each as you remove
# them.

list = [1,2,3,4,5]
print(list[4])
del list[4]
print(list[3])
del list[3]
print(list)


#######################################################################################
# 10.14
# Use the "in" operator to check if a value is in a list. Use an if statement here.

list = [1,2,3,4,5]
if 1 in list:
    print(str(1) + ' is in the list')
else:
    print(str(1) + ' is not in the list')

if 6 in list:
    print(str(6) + ' is in the list')
else:
    print(str(6) + ' is not in the list')

