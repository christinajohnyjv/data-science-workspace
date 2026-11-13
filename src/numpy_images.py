# 2D OCT Image Patch Processing
import numpy as np

oct_patch = np.array([
    [30,  45,  50,  60],
    [70,  85,  90, 110],
    [120, 140, 155, 170],
    [180, 200, 220, 255]
])
print("Shape of the array:",oct_patch.shape)
print("Total number of pixels:",oct_patch.size)

# Pixel Normalization
norm=oct_patch/255
normalization=np.round(norm,2)
print("\nNormalization of the pixel:\n", normalization)

# Matrix Slicing
# 1. Crop the center 2x2 patch
center_roi = oct_patch[1:3, 1:3]
print("\nCenter 2x2:\n", center_roi)
# 2. Extract just the top row (Row 0, all columns)
top_r=oct_patch[0,:]
print("\nTop Row:\n",top_r)
# 3. Extract just the first column (all rows, Col 0)
first_c=oct_patch[:,0]
print("\nFirst Column:\n",first_c)

# Boolean Masking
bright_pixels = oct_patch[oct_patch >= 150] # creates a True/False grid 
mean_B=round(np.mean(bright_pixels),2)
dark_pixels=oct_patch[oct_patch<50]
mean_d=round(np.mean(dark_pixels),2)
print("\nBright Pixels:\n", bright_pixels) # NumPy instantly extracts only the True numbers
print("\n Mean of the bright Pixels:", mean_B)
print("\nDark Pixels:\n", dark_pixels)
print("\n Mean of the Dark Pixels:", mean_d)