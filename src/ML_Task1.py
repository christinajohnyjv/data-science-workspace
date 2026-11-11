# Confidence Analyzer
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