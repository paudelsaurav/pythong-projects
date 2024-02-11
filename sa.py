from collections import Counter

num_list = [1, 2, 1, 3, 10, 9, 8, 4, 5, 7, 1, 2, 4, 8, 5, 9, 6, 6, 3]

# Use Counter to count the frequency of each item in the list
frequency_counter = Counter(num_list)

# Find the number with the highest frequency
most_common_number, highest_frequency = frequency_counter.most_common()

# Print the results
print("Frequency of each item:")
for number, frequency in frequency_counter.items():
    print(f"{number}: {frequency}")

print(f"\nThe number with the highest frequency is {most_common_number} with a frequency of {highest_frequency}.")
