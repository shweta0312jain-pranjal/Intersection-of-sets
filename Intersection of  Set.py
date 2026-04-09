set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

intersection = set1.intersection(set2)

total_guests = list(intersection)

print("Total guests invited to the party:", len(total_guests))
print("List of guests invited to the party:", total_guests)