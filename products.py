products = []
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter product price: ')
	products.append([name, price])
for p in products:
	print('the price of', p[0], 'is', p[1])