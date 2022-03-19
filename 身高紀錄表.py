import os 
length = []
if os.path.isfile('length.csv') :
	print('找到檔案了')
	with open('length.csv','r',encoding='utf=8') as g :
		for line_1 in g :
			if '姓名,身高(cm)' in line_1 :
				continue
			x = line_1.strip().split(',')
			length.append([x[0],x[1]])
else :
	print('找不到檔案qq')

print(length)
while True :
	name = input('輸入姓名:')
	if name == '0' :
		break
	tall = input('輸入身高(cm):')
	length.append([name,tall])
print(length)
for y in length :
	print(y[0],'的身高為',y[1])

with open('length.csv','w',encoding = 'utf_8') as f :
	f.write('姓名,身高(cm)\n')
	for line_2 in length :
		f.write(line_2[0]+','+line_2[1]+'\n')