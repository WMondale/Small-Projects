#Will McKnight
#Takes an input base n and an output base m, both from 2 to 16, and a number in
#base n as input.  Returns a number base m as output.  It should be noted that
#while the input and output are intended as in their respective bases, the data
#type is still int.

#string list of all characters for base 16
base=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

#obtain input base
n=0
while n<2 or n>16 or n%1!=0:
	n=int(input("Please input the base of your number from 2 to 16:\n"))

#obtain output base
m=0
while m<2 or m>16 or n%1!=0:
	m=int(input("Please input the desired output base from 2 to 16:\n"))

#obtain input number, check if it's valid for the input base
valid=False
while not valid:
	inum=str(input("Please input number in correct input base (letters must be lowercase):\n"))
	for c in inum:
		for d in base[0:n]:
			if c==d:
				valid=True
				break
		if not valid:
			break

#make base 10 intermediate variable
inter=0
#count through input "number" (actually a string), translate to base-10
for x in range(0,len(inum)):
	for y in range(1,n):
		if inum[::-1][x]==base[y]:
			inter=inter+(n**(x)*y)
			break
#find output base form of number
a=0
b=0
outbase=[]
#find spaces required for output and create "blank" string
while a<=inter/m:
	b=b+1
	a=m**b
for x in range(0,b+1):
	outbase.append("0")
#find maximum exponent of base number under the intermediate, then multiply
#the resultant number to the maximum extent.  Exponent determines position in
#outbase string
a=0
b=0
z=0
while inter>=m:
	while a<=inter/m:
		b=b+1
		a=m**b
	origa=a
	while a<=inter:
		z=z+1
		a=origa*z
	outbase[b]=base[z-1]
	inter=int(inter-(a-origa))
	a=0
	b=0
	z=0
outbase[0]=base[inter]
out="".join(outbase[::-1])
print(out)
