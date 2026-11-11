# Clinical Patient Temperature Monitor
def filter_valid_readings(readings, min_valid, max_valid):
    clean_readings=[]
    for t in readings:
        if min_valid<=t<=max_valid:
            clean_readings.append(t)
    return clean_readings    
def analyze_fever_status(clean_readings, fever_threshold):
    fever_cases = []
    normal_cases = []
    for c in clean_readings:
        if c >= fever_threshold:
            fever_cases.append(c)
        else:
            normal_cases.append(c) 
    avg_temp = round(sum(clean_readings)/len(clean_readings), 2)    
    fever_pct = round((len(fever_cases)/len(clean_readings)*100),1)       
    return fever_cases, normal_cases, avg_temp, fever_pct
raw_temps = [36.5, 37.2, -99.0, 38.5, 36.8, 41.0, 0.0, 39.1]
clean = filter_valid_readings(raw_temps, 30.0, 45.0)
print("Clean readings:", clean)
fever, normal, avg_t, pct = analyze_fever_status(clean, 38.0)
print("Fever cases:", fever)
print("Normal cases:", normal)
print(f"Average temp: {avg_t}°C")
print(f"Fever rate: {pct}%")