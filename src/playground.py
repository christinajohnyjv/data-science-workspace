# Enter the Input values
scores=[45, 82, 90, 68, 55, 94, 72]
# Find the highest score
print("The highest score is ", max(scores))
# Find the lowest score
print("The lowest score is ", min(scores))
# Find the average score
#a=sum(scores)
#b=len(scores)
#c=a/b
print("The average score is ", sum(scores)/len(scores))

# for Loops (for) and Conditions (if / else)
passing_scores=[]
failing_scores=[]
for a in scores:
    if a >= 70:
        passing_scores.append(a)
    else:
        failing_scores.append(a)  
print("Passing scores:", passing_scores)
print("Failing scores:", failing_scores)
print("Number of students passed:", len(passing_scores))        
print("Average score of the passing students:", sum(passing_scores)/len(passing_scores))