
myfile = open("fruits.txt")
content = myfile.readlines()
myfile.close()
for apa in content:
	panjang = str(apa)
	print(len(panjang)-1)

"""
Blackpink = [3,4,6,11,2,17,90]
for i in Blackpink:
	if(i>5):
		print(i)
"""
