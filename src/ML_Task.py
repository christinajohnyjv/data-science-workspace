# ML Data Imputation & Normalization
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

#API Server Response Latency Pipeline
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