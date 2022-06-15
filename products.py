products = []
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter product price: ')
	products.append([name, price])
for p in products:
	print('the price of', p[0], 'is', p[1])
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')