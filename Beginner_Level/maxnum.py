if:
	n1=int(input())
	n2=int(input())
	while(n2!=0):
		t=n2
		n2=n1%n2
		n1=t
	print(n1)
else:
	print('invalid')
