import os #載入作業系統

# 讀取檔案，並把原有檔案加入 products 清單
def read_file(filename, products_list): 
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products_list.append([name, price])
	return products_list

# 請使用者輸入商品與價格並存到 products 清單
def user_input(products_list):
	while True:
		name = input('please enter product name: ')
		if name == 'q':
			break
		price = input('please enter product price: ')
		products_list.append([name, price])
	return products_list

# 顯示商品價格
def show_price(products_list):
	for p in products_list:
		print('the price of', p[0], 'is', p[1])

# 寫入商品價格
def write_file(products_list):
	with open('products.csv', 'w', encoding='utf-8') as f:
		f.write('product,price\n')
		for p in products_list:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	products = []
	if os.path.isfile('products.csv'): # 檢查有無 products.csv 檔案
		print('file found')
		products = read_file('products.csv', products)
	else:
		print('file not found')
	products = user_input(products)
	show_price(products)
	write_file(products)

main()