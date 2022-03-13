cm=float(input('請輸入你的身高:'))
kg=float(input('請輸入你的體重:'))
tall=cm/100
bmi=round(kg/(tall**2),2)
print('你的bmi:',bmi)
if bmi<18.5 :
	print('體重過輕')
elif bmi>=18.5 and bmi<24:
	print('體重正常')
elif bmi>=27 and bmi<30:
	print('輕度肥胖')
elif bmi>=30 and bmi<35:
	print('中度肥胖')
else:
    print('重度肥胖')