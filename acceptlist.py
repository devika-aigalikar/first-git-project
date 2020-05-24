"""# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  # adding the element

print(lst)
"""
lst = []
n = int(input('Enter number of elements : '))
for i in range(n):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))

