# # Leap Year
# def is_leap(year):
#     leap=False
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap=True
#     return leap
# year = int(input("Enter the year:"))
# print(is_leap(year))

# # Print the string 
# n = int(input("Enter the number for string:"))
# for i  in range(1,n+1):
#     print(i,end="")

# # Divmod
# a=int(input("\nA:Enter the number for Divmod:"))
# b=int(input("B:Enter the number for Divmod:"))
# print(a//b)
# print(a%b)
# print(divmod(a,b))

# # Generate a list of 3D coordinates [i, j, k] and filter out the ones whose sum equals a given number n
# x = int(input("X:Enter the number for 3D coordinates: "))
# y = int(input("Y:Enter the number for 3D coordinates: "))
# z = int(input("Z:Enter the number for 3D coordinates: "))
# n = int(input("N:Enter the number for 3D coordinates: "))
# result=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#            if i+j+k!=n:
#               result.append([i,j,k])
# print(result)     

# Find the Runner-Up Score
n = int(input("Enter the number of items in list: "))
arr = map(int, input("Enter the numbers:").split())
unique_sorted = sorted(set(arr))
print(unique_sorted[-2])
