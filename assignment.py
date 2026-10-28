def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    return min(values), max(values), sum(values)


number_of_days = int(input("Enter the number of days: "))

original = []
for i in range(number_of_days):
    puzzles = int(input("Enter the number of puzzles solved: "))
    original.append(puzzles)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of puzzles: "))
replace_value(updated, index, new_value)

target = int(input("Enter the number of puzzles to search for: "))

first_index = find_first(updated, target)
match_count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_values = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum number of puzzles: {minimum}")
print(f"Maximum number of puzzles: {maximum}")
print(f"Total number of puzzles: {total}")
if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")
print(f"Matching values: {match_count}")
