# ASCI Value

var = 65
for i in range(1 , 6):
	for j in range( 1 , i +1):
		ch = chr(var)
		print(ch , end=" " )
	var += 1
	print()