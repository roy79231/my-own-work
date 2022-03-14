import random
while True :
    start = int(input('請你輸入開始範圍值:'))
    end = int(input('請你輸入結束範圍值:'))
    if end > start :
    	break
    elif end <= start :
    	print('開始值要小於結束值喔!')

r = random.randint(start,end)
count = 0
while True :
	num = int(input('請猜數字:'))
	count = count +1
	if num == r :
		print('恭喜答對!')
		break
	elif num < r :
		print('請猜大一點')
	elif num > r :
		print('請猜小一點')
	print('這是你猜的第',count,'次')