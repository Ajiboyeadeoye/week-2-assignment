# Create empty list
my_list = []
#Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert value 15 at the second position of the list
my_list.insert(1, 15)
#Extend my_list
my_list.extend([50, 60, 70])
#Remove the last element 
my_list.pop()
#Sort the elements
my_list.sort()
#Find and print index of element 30
index = my_list.index(30)
print('Index of 30: ', index)


print('Elements of the list: ', my_list)

