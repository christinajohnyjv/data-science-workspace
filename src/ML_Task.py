# 1. ML Data Imputation & Normalization
raw_features = [10.0, 20.0, -99.0, 30.0, 999.0, 40.0]
# Find the Mean of Only Valid Data
valid_features = []
for r in raw_features:
    if 0 <= r <=100:
        valid_features.append(r)
print("Valid features:", valid_features)        
mean_value=sum(valid_features)/len(valid_features)
print("Average Value:", mean_value)
# Outlier Imputation
clean_features = []
for r in raw_features:
    if 0 <= r <=100:
        clean_features.append(r)
    else:
        clean_features.append(mean_value)   
print("Clean features (with outliers replaced):", clean_features)
# Min-Max Normalization
min_val=min(clean_features)
max_val=max(clean_features)
normalized_features = []
for r in clean_features:
    scaled = (r-min_val)/(max_val-min_val)
    normalized_features.append(round(scaled,2))
print("Normalized features (between 0 and 1): ", normalized_features)

# 2. API Server Response Latency Pipeline
raw_latencies = [120, 150, -5, 180, 2000, 150]
valid_latencies = []
for l in raw_latencies:
    if 5 <= l <= 500:
        valid_latencies.append(l)
mean_latency=sum(valid_latencies)/len(valid_latencies)
print("Valid latencies: ",valid_latencies)
print("Average latency: ",mean_latency)

clean_latencies = []
for l in raw_latencies:
    if 5 <= l <= 500:
        clean_latencies.append(l)
    else:
        clean_latencies.append(mean_latency)    
print("Clean latencies: ", clean_latencies)    

normalized_latencies=[]
for l in clean_latencies:
    scaled= (l-min(clean_latencies))/(max(clean_latencies)-min(clean_latencies))
    normalized_latencies.append(round(scaled,2))
print("Normalized latencies: ", normalized_latencies)   

# 3. Confidence Analyzer
raw_confidences = [88.5, 94.0, -1.0, 72.5, 105.0, 45.0, 91.0, 60.0]
# Data Cleaning
valid_confidences = []
for c in raw_confidences:
    if 0<=c<=100:
        valid_confidences.append(c)
print("Valid scores: ", valid_confidences)
print("Average confidence: ", round(sum(valid_confidences)/len(valid_confidences),2))        
# Clinical Triage (Categorization)
high_confidence=[]
moderate_confidence=[]
low_confidence=[]
for c in valid_confidences:
    if c >= 85.0:
        high_confidence.append(c)
    elif 60 <= c <= 85.0:
        moderate_confidence.append(c)
    else:
        low_confidence.append(c)
print("High confidence :", high_confidence, "Highest:", max(high_confidence))                
print("Moderate confidence :", moderate_confidence)
print("Low confidence:", low_confidence, "Lowest:", min(low_confidence))
print("Total requiring doctor attention: ", len(moderate_confidence)+len(low_confidence))