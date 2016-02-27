def hello(imie):
	#print('Hello ' + imie)
	#print("Django Girls!")
	if imie=="Michał":
		print("Hello " + imie)
	#else:
	#	print("Hello")
	elif not imie.endswith('a'):
		print ("For girls only!")
	else:
		print ("Nie znam cię")
hello("Michalina")

oceny=[2,3,4,5,6,2,3,4,1]
def print_list (l):
	for element in l:
		print (element)
		print("-"*10)

print_list(oceny)


for a in range(6):
	print(a)

