#!/usr/bin/env python3

from math import pi as PI
import numpy as np
from numpy import linalg as la
#from scipy import linalg as la

# Calculate Circumference
C = 2 * 0.43 * PI
# Calculate Area
A = PI * 0.43 ** 2

print(f"Circumference: {C}")
print(f"Area: {A}")

np_arr1 = np.array([True, 1, 2]) 
np_arr2 = np.array([3, 4, False])
print(np_arr1 + np_arr2)

weights_lb = list(range(180, 210, 2))
print(weights_lb)
np_weights_lb = np.array(weights_lb)
print(type(np_weights_lb))
print(np_weights_lb)

# height in inch, weight in pounds (lb), age in year
baseball = [[74.0, 180.0, 22.99],
            [74.0, 215.0, 34.69],
            [72.0, 210.0, 30.78],
            [69.0, 209.0, 30.77],
            [71.0, 200.0, 35.07],
            [76.0, 231.0, 30.19]]
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

# height in inch, weight in pounds (lb), age in year
updated_list = [[  1.2303559 , -11.16224898,   1.        ],
                [  1.02614252,  16.09732309,   1.        ],
                [  1.1544228 ,   5.08167641,   1.        ],
                [  1.09349925,   4.23890778,   1.        ],
                [  0.82285669, -17.78200035,   1.        ],
                [  0.99484223,   8.14402711,   1.        ]]
np_updated = np.array(updated_list)
np_baseball += np_updated
print(np_baseball)
# Conversion: inch-to-meter, lb-to-kg, yr-to-yr
conversion = np.array([0.0254, 0.453592, 1])
np_baseball *= conversion
print(np_baseball)

np_heights = np.round(np.random.normal(1.75, 0.20, 5000), 2)
np_weights = np.round(np.random.normal(60.32, 15, 5000), 2)
np_citizens = np.column_stack((np_heights, np_weights))
print(np_citizens.shape)
print(f"mean of heights: {np.mean(np_citizens[:, 0])}")
print(f"median of heights: {np.median(np_citizens[:, 0])}")
print(f"std deviation of heights: {np.std(np_citizens[:, 0])}")
print(f"mean of weights: {np.mean(np_citizens[:, 1])}")
print(f"median of weights: {np.median(np_citizens[:, 1])}")
print(f"std deviation of weights: {np.std(np_citizens[:, 1])}")
print(f"correlation coeff of heights and weights: {np.corrcoef(np_citizens[:, 0], np_citizens[:, 1])}")
print(f"std deviations of heights and weights: {np.std(np_citizens, 0)}")
