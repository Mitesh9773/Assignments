# Write a Python program to count how many times each
# character appears in a string.

myStr = "Hello My name is Mitesh Rathod"
myStr = myStr.lower()
myDict = {}

for ch in myStr:
    if ch not in myDict:
        myDict[ch] = myStr.count(ch)

for key,value in myDict.items():
    print(f"{key} : {value}")

