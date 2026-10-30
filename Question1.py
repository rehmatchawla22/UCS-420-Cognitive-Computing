
import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# a. Add 2°C to every reading using vectorization
corrected_temperature = temperature + 2
print("Corrected temperatures:", corrected_temperature)

# b. Convert Celsius to Fahrenheit
fahrenheit = (corrected_temperature * 9 / 5) + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# c. Identify readings greater than 32°C
readings_above_32 = corrected_temperature[corrected_temperature > 32]
print("Readings greater than 32°C:", readings_above_32)

# d. Count readings greater than 32°C
count = np.sum(corrected_temperature > 32)
print("Count of readings greater than 32°C:", count)

# e. Explanation
print("\nVectorization performs operations on entire arrays without using a for loop.")
print("Boolean indexing selects elements based on conditions.")
