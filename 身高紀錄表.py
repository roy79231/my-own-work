import os 
def file_check(filename):
	length = []
	with open(filename,'r',encoding='utf=8') as g :
		for line_1 in g :
			if '姓名,身高(cm)' in line_1 :
				continue
			x = line_1.strip().split(',')
			length.append([x[0],x[1]])
		return length	
def user_input(length):
	print(length)
	while True :
		name = input('輸入姓名:')
		if name == '0' :
			break
		tall = input('輸入身高(cm):')
		length.append([name,tall])
	print(length)
	return length
def content_check(length): 	
	for y in length :
		print(y[0],'的身高為',y[1])
def content_inport(filename,length):
	with open(filename,'w',encoding = 'utf_8') as f :
		f.write('姓名,身高(cm)\n')
		for line_2 in length :
			f.write(line_2[0]+','+line_2[1]+'\n')
def main():
	filename = 'length.csv'
	if os.path.isfile(filename) :
		print('找到檔案了')
		length = file_check(filename)
	else :
		print('找不到檔案qq')
	length = user_input(length)
	content_check(length)
	content_inport(filename,length)

main()