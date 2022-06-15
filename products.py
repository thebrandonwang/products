products = []

# 讀取檔案，並把原有檔案加入products清單
with open('product.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'product,price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

# 請使用者輸入商品與價格並存到products清單
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter product price: ')
	products.append([name, price])

# 顯示商品價格
for p in products:
	print('the price of', p[0], 'is', p[1])

# 寫入商品價格
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')