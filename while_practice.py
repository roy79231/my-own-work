#複習else elif and while
#問使用者最喜歡的顏色
#答案為藍色 且只有3次機會
x = 3
while True :
	color = input('你最喜歡的顏色是?')
	if color == '藍色':
		print('恭喜你答對了')
		break
	elif color == '青色' :
		print('答案很接近了')
		x = x-1 
		if x <= 0 :
			break
		print('你還有',x,'次機會')
	else :
		print('你答錯了')
		x = x-1
		if x <= 0 :
			break
		print('你還有',x,'次機會')
