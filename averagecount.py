ch=int(input('請輸入你的國文成績:'))
math=int(input('請輸入你的數學成績:'))
english=int(input('請輸入你的英文成績:'))
science=int(input('請輸入你的自然成績:'))
social=int(input('請輸入你的社會成績'))
average=round((ch+math+english+science+social)/5,1)
print('你的段考平均:',average)