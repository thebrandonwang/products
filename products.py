import os #載入作業系統
products = []

# 檢查有無 products.csv 檔案
if os.path.isfile('products.csv'):
	print('file found')
	# 讀取檔案，並把原有檔案加入 products 清單
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('file not found')

# 請使用者輸入商品與價格並存到 products 清單
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
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')