from collections import Counter

List1 = [3, 5, 2, 8]
List2 = [1, 2, 5, 2, 8, 5, 3, 2]

# Create a Counter object for List2
counter = Counter(List2)

# Create a new list where each element corresponds to the count of List1 elements in List2
count_list = [counter[element] for element in List1]

print(count_list)