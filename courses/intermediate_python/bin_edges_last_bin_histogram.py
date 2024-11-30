import numpy as np
import matplotlib.pyplot as plt

# Demonstrate bin inclusivity
print("\nDemonstrating bin inclusivity:")
test_arr = np.array([0, 1, 1.9, 2, 2.9, 3])  # test values at bin edges

counts, bins, _ = plt.hist(test_arr, bins=3)

print("Test values:", test_arr)
print("Bin edges:", bins)
print("Counts in each bin:", counts)

# Print which values go into which bins
for i in range(len(bins) - 1):
    bin_values = test_arr[(test_arr >= bins[i]) & (test_arr < bins[i + 1])]
    print(f"Values in bin [{bins[i]}, {bins[i+1]}): {bin_values}")

# Last bin includes right edge
last_bin_values = test_arr[(test_arr >= bins[-2]) & (test_arr <= bins[-1])]
print(f"Values in last bin [{bins[-2]}, {bins[-1]}]: {last_bin_values}")

plt.show()
