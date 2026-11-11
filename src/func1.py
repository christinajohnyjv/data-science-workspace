def normalize_data(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    scaled_list = []
    for n in numbers:
        m = (n-min_val)/(max_val-min_val)
        scaled_list.append(round(m,2))
    return scaled_list
exam_scores = [20, 40, 60, 80, 100]
result = normalize_data(exam_scores)    
print("Original:", exam_scores)
print("Normalized:", result)