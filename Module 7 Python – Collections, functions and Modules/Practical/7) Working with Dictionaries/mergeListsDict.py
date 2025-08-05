# Write a Python program to merge two lists into one dictionary using a loop.

list1 = ['M','P','J','K']
list2 = [4,4,3,2]


newDict = {}

if  len(list1) == len(list2):
    for i in range(len(list1)):
        newDict[list1[i]] = list2[i]
else:
    print("Lists are not of equal length")

for key, value in newDict.items():
    print(f"{key}: {value}")
