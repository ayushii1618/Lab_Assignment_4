import numpy as np
from collections import Counter

# Print numpy version
print("Numpy version:", np.__version__)

# Take input list from user
user_input = input("Enter a list of integers/characters separated by space: ").split()
freq = Counter(user_input)

print("Frequency of each element:", dict(freq))
