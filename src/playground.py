# # Enter the Input values
# scores=[45, 82, 90, 68, 55, 94, 72]
# # Find the highest score
# print("The highest score is ", max(scores))
# # Find the lowest score
# print("The lowest score is ", min(scores))
# # Find the average score
# #a=sum(scores)
# #b=len(scores)
# #c=a/b
# print("The average score is ", sum(scores)/len(scores))

# # for Loops (for) and Conditions (if / else)
# passing_scores=[]
# failing_scores=[]
# for a in scores:
#     if a >= 70:
#         passing_scores.append(a)
#     else:
#         failing_scores.append(a)  
# print("Passing scores:", passing_scores)
# print("Failing scores:", failing_scores)
# print("Number of students passed:", len(passing_scores))        
# print("Average score of the passing students:", sum(passing_scores)/len(passing_scores))

# #Lab Temperature Sensor Readings
# temperatures = [22.5, 23.1, 28.4, 21.8, 30.2, 24.0, 29.5]
# alert_temps = []
# normal_temp = []
# for t in temperatures:
#     if t >= 28.0:
#         alert_temps.append(t)
#     else:
#         normal_temp.append(t)       
# print("Overheating Alert:", alert_temps)
# print("Normal Temp: ", normal_temp)
# print("Number of times the sensor triggered an alert:", len(alert_temps))
# print("The average of the normal temperatures:", sum(normal_temp)/len(normal_temp))

# Outlier Filter
batch_losses = [1.2, 0.8, 4.5, 0.6, 0.5, 3.9]
# Overall average loss of all 6 batches
print("Average loss:", round(sum(batch_losses) / len(batch_losses), 2))
good_loss=[]
high_loss=[]
for b in batch_losses:
    if b <= 1.0:
        good_loss.append(b)
    else:
        high_loss.append(b)
print("Good Losses:", good_loss)
print("High Losses:", high_loss)
print("Lowest loss achieved among the good losses:", min(good_loss))
print("Average of the good losses:", sum(good_loss)/len(good_loss))