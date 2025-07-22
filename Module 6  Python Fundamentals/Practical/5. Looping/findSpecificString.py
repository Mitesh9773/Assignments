# Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition

name = ["Mitesh", "Sujal", "Manthan"]
search_name = "Manthn"

found = False

for i in range(len(name)):
    if name[i] == search_name:
        print(f"Found {search_name} at index {i}")
        found = True
        break

#If not found at all, print message

if not found:
    print(f"{search_name} not found in the list")
