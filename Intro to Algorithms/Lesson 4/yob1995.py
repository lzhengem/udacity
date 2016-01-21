# Use this file to find the second most 
# common popular female name: yob1995.txt

females = []
#open the file and save all females into females list
with open("yob1995.txt") as file:
    for line in file:
        person = line.strip().split(",")
        if person[1] == "F": females.append(person)
#sort the females by the index 2, which is the occurences of that name 
females.sort(key=lambda x: int(x[2]), reverse=True)

#the female at index 1 is the 2nd most common female name
print(females[1])
