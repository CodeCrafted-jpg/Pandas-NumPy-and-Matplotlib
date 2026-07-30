list=[1, 2, 1]

copy_list=list.copy()
copy_list.reverse()

if(list==copy_list):
    print("The list is a palindrome")

else:
    print("The list is not a palindrome")