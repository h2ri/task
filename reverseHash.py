print "Please Enter the hash"
n=int(input().strip())
str1 = 'acdegilmnoprstuw'
str2=''
for i in range(0,9):
	temp=n%37
	str2=str2+str1[temp];
	n=n//37
print(str2[::-1])  
