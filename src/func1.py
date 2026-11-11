# # Normalization
# def normalize_data(numbers):
#     min_val = min(numbers)
#     max_val = max(numbers)
#     scaled_list = []
#     for n in numbers:
#         m = (n-min_val)/(max_val-min_val)
#         scaled_list.append(round(m,2))
#     return scaled_list
# exam_scores = [20, 40, 60, 80, 100]
# result = normalize_data(exam_scores)    
# print("Original:", exam_scores)
# print("Normalized:", result)

# Disease Detected
def evaluate_predictions(probabilities, threshold):
    positive_cases = []
    negative_cases = []
    for p in probabilities:
        if p>=threshold:
            positive_cases.append(p)
        else:
            negative_cases.append(p)
        detection_rate=round((len(positive_cases)/len(probabilities))*100, 1)        
    return positive_cases, negative_cases, detection_rate
model_outputs = [0.92, 0.45, 0.88, 0.74, 0.31, 0.95, 0.60]
cutoff = 0.70
a,b,c = evaluate_predictions(model_outputs, cutoff)    
print("Positive cases:", a)
print("Negative cases:", b)
print("Detection rate:", c)