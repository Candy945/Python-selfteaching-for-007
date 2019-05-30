print('欢迎使用糖果简易计算器1.0')         # 界面提示

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if choice == '1':
    print(a, "+", b, "=", a+b)
elif choice == '2':
    print(a, "-", b, "=", a-b)
elif choice == '3':
    print(a, "*", b, "=", a*b)
elif choice == '4':
    print(a, "/", b, "=", a/b)
else:
    print("Invalid input")





print('欢迎使用糖果简易计算器2.0')         # 界面提示
print('-------------------')
# while True :
#    a = input('请输入等式【退出计算器请输入y】:')
    
#    if a == y
#        print("谢谢使用!")
#        break
#    elif a:
#        print(a)
#        continue
#    else:
#        print("输入错误")
#        continue
        
#print('-------------------')
 


