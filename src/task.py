# Retinal Thickness Diagnostic Pipeline
def clean_and_impute(data, min_valid, max_valid):
    valid_num=[]
    valid_no=[]
# Calculate Mean of Valid Data    
    for d in data:
        if min_valid<d<max_valid:
            valid_num.append(d)
    num_mean=round(sum(valid_num)/len(valid_num),1) 
#Impute Corrupted Glitches     
    for i in data:
        if i<min_valid:
            valid_no.append(num_mean)
        elif i>max_valid:
            valid_no.append(num_mean)
        else:
            valid_no.append(i)                      
    return valid_no, num_mean

# Triage into 3 Categories
def triage_and_analyze(clean_data, low_threshold, high_threshold):
    atrophy=[]
    edema=[]
    normal=[]
    for i in clean_data:
        if i < low_threshold:
            atrophy.append(i)
        elif i > high_threshold:
            edema.append(i) 
        else:
            normal.append(i)
# Metrics            
    normal_avg =  round(sum(normal)/len(normal),1) 
    highest_val = max(clean_data)
    lowest_val = min(clean_data)      
    return atrophy, edema, normal, normal_avg, highest_val, lowest_val              

raw_oct_readings = [110, 80, -999, 130, 40, 0, 150, 90]
clean, mean = clean_and_impute(raw_oct_readings,1,200)
atr, edem, norm, norm_avg, higval, lowval = triage_and_analyze(clean, 75, 140)
print("Cleaned scans: ", clean)
print("Imputed mean: ", mean)
print("Normal Sectors:", norm)
print("Atrophy:", atr)
print("Edema:", edem)
print("Normal Sector Average: ", norm_avg)
print("Highest :", higval, "Lowest: ", lowval)
