cm=int(input('請輸入你的身高:'))
kg=int(input('請輸入你的體重:'))
tall=cm/100
bmi=round(kg/(tall**2),2)
print('你的bmi:',bmi)