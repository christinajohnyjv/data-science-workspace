# Leap Year
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    return leap
year = int(input())
print(is_leap(year))

# Print the string 
n = int(input())
for i  in range(1,n+1):
    print(i,end="")

# Divmod
a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

# Generate a list of 3D coordinates [i, j, k] and filter out the ones whose sum equals a given number n
x = int(input())
y = int(input())
z = int(input())
n = int(input())
result=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
           if i+j+k!=n:
              result.append([i,j,k])
print(result)     