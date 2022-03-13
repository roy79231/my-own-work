#預設密碼為a123456789 讓使用者最多輸入3次密碼 
#如果不對會顯示剩幾次機會
x=3
while True: 
    password = input('請輸入您的密碼:')
    if password == 'a123456789' :
    	print('登入成功!')
    	break
    else :
    	x=x-1
    	print('你的密碼錯誤，您剩餘', x,'次機會')
    	if x<= 0:
    		print('登入失敗')
    		break


