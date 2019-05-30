
print('欢迎使用糖果简易计算器')         # 界面提示
print('-------------------')
while True:
    a = input('请输入等式（退出计算器请输入y）： ')
    
    if a == 'y' :
        print("谢谢使用!")
        break
    elif a:
        print(a)
    else:
        print("输入错误")
        
print('-------------------')
 


