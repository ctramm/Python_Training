# Python code to demonstrate the working of pop() and remove() with arrays

import array

arr = array.array('i', [1, 2, 3, 1, 5])

print("The newly created array is : ", end="")
for i in range (0,5):
    print(arr[i], end=" ")
print("\r")

# Using pop() to remove element at 2nd position
print("The popped element is :", end="")
print(arr.pop(2))

# Printing array after popping
print("The array after popping is: ", end="")
for i in range (0,4):
    print(arr[i],end=" ")
print("\r")

# Using remove() to remove 1st occurrence of 1
arr.remove(1)

# Printing after removing
print("The array after removing is : ", end="")
for i in range(0,3):
    print(arr[i], end=" ")

