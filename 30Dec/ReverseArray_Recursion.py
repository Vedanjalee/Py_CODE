def reverse(n,left, right):
    if left >= right:
        return 
    
    n[left], n[right] = n[right], n[left]
    reverse(n, left + 1, right -1 )

my_list = [1, 2, 3, 4, 5]
print("Original list ", my_list)
left =  0 
right = len(my_list) - 1

reverse(my_list, left, right)
print(my_list)