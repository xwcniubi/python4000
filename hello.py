print('hello world')
num = int(input('请输入一个整数:'))
for i in range(2,num+1):
    if num%i==0:
    	break
else:
    print('是质数...')
