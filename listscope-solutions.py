#create a list called my_list
my_list = [1,2,3,4]

#do not change
print('my_list before calling edit_entry is %s' %my_list)

def edit_entry(a_list, index, new_element):

    '''
    changes the element of a list at a specific index to a specified new element
    '''

    a_list[index] = new_element

    return

#call edit_entry with your list as an argument
#change the 5th entry of the list from its current value to 42
edit_entry(my_list, 2, 45)

#do not change
print('my_list after calling edit_entry is %s' %my_list)
