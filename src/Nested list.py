names=[]
bonus=[]
for i in range (int(input("Enter the number of employees: "))):
    name=input("Enter the name of the Employee: ")
    score=int(input("Enter the bonus amount: "))
    names.append(name)
    bonus.append(score)
# Find the second highest Bonus
unique_bonus=sorted(set(bonus))
second_highest=unique_bonus[-2]
# Sort the employees in alphabetical order
result=[]
for j in range(len(names)):
    if bonus[j] == second_highest:
        result.append(names[j])
result.sort()
for r in result:
    print(r)
    