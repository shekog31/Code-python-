import array as arr

an=arr.array("i", [1,2,3,4,5,6,3,4,2])
print("Original array:" +str(an))

print("Number of occurrences of the number 3 in the array:" +str(an.count(2)))

an.reverse()
print("reverse the order of the items:")
print(str(an))