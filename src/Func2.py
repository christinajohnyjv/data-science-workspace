# 1. Clinical Patient Temperature Monitor
print("---------Clinical Patient Temperature Monitor-----------")
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

# Clean the data
clean = filter_valid_readings(raw_temps, 30.0, 45.0)
print("Clean readings:", clean)

# Analyze fever cases
fever, normal, avg_t, pct = analyze_fever_status(clean, 38.0)
print("Fever cases:", fever)
print("Normal cases:", normal)
print(f"Average temp: {avg_t}°C")
print(f"Fever rate: {pct}%")

# 2. Image Pixel Clipper & Scaler
print("\n---------Image Pixel Clipper & Scaler-----------")
def clip_intensities(pixels, min_val, max_val):
    clipped_pixels=[]
    for p in pixels:
        if p < min_val:
            clipped_pixels.append(min_val)
        elif p > max_val:
            clipped_pixels.append(max_val)    
        else:
            clipped_pixels.append(p)    
    return clipped_pixels
def scale_to_percentage(clipped_pixels, max_scale):
    scaled_pixels=[]
    for i in clipped_pixels:
        scaled = round((i/max_scale)*100,1)
        scaled_pixels.append(scaled)
    return scaled_pixels

raw_pixels = [15, 40, -10, 80, 120, 50]

# Clip between 0 and 100
clipped = clip_intensities(raw_pixels, 0, 100)
print("Clipped pixels:", clipped)

# Scale with max_scale = 100.0
scale=scale_to_percentage(clipped, 100)    
print("Scaled Percentage:", scale)