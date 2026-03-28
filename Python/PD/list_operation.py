my_list = [19,19.5,30,60]
new_index =1 
old_index = 3

e = my_list.pop(old_index)

if my_list == 0:
    print("List is empty")
else:
    print("List is here!")
    print("The length of list =",len(my_list))
    print("The orginal List =",my_list)
    my_list.append(39)
    print("New List =",my_list)
    my_list.insert(new_index,e)
    print("Manipulated List =",my_list)
    my_list.reverse()
    print("Reversed List",my_list)

