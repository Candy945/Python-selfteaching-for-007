# 使用Python的for...in循环,打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=" ")
    print()

# 用Python的while循环,打印九九乘法表,并用条件判断把偶数行去掉
i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j < i + 1:
        print("{}*{}={}".format(i,j,i*j),end=" ")
        j += 1
    print()
    i += 1
