#1、创建 Day5_exercise_array.py 文件
#2、将数组[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]翻转
#3、翻转后的数组拼接成字符串
#4、用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
#5、将获得的字符串进行反转
#6、将结果转换为int类型
#7、分别转换成二进制，八进制，十六进制
#8、最后输出三种进制的结果

# [Python list/str类型相互转换](https://blog.csdn.net/qq_14997473/article/details/86515610)



a_list=[0,1,2,3,4,5,6,7,8,9]
print(a_list)

a_list.reverse()        ##翻转数组
print(a_list)

c=''.join(map(str,a_list))      # 拼接成字符串 list(元素是int型)，因为join函数的对象应该是str而不能是int，需要借助map()函数将list内每个元素转为str型，再join().
print(c)

d=c[2:8]            # #用字符串切片的方式取出第三到第八个字符（包含第三和第八个字符）
print(d)

t=int(d[::-1])      # 将获得的字符串反转，转换为int类型

print('十进制：',t)
print('二进制：',bin(t))        #转换成二进制并输出
print('八进制：',oct(t))        #转换成八进制并输出
print('十六进制：',hex(t))        #转换成十六进制并输出











