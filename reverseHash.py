print "Please Enter the hash"
n=int(input().strip())
str1 = 'acdegilmnoprstuw'
str2=''
for i in range(0,9):
	temp=n%37
	print temp
	print "\n"
	str2=str2+str1[temp];
	n=n//37
	if n == 7:
		break;
print(str2[::-1])
#For 930846109532517 the string is lawnmower  
