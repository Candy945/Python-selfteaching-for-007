#1、创建 Day5_exercise_string.py 文件
#2、将字符串样本text里英文单词better全部替换成worse
#3、从上一步结果里，将单词中包含 ea 的单词剔除
#4、将上一步结果里的字母进行大小写转换（将大写字母转成小写，小写字母转成大写）
#5、将上一步结果里所有单词按 a…z 升序排列
#6、最后输出结果
# 2019/06/03

text = ''' The Zen of Python, by Tim Peters

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambxiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!

'''


# 将字符串样本text里英文单词better全部替换成worse

if 'better' in text:
    s=text.replace('better','worse')
s               # 显示 字符串 s

# 从上一步结果里，将单词中包含 ea 的单词剔除

a_list=s.split()        # split() 是将一个字符串根据分隔符进行拆分，返回一个列表
a_list                  # 显示 列表a_list

# 清洗列表
a_list=[x.strip(',') for x in a_list]
a_list=[x.strip('.') for x in a_list]
a_list=[x.strip('-') for x in a_list]
a_list=[x.strip('*') for x in a_list]
a_list=[x.strip() for x in a_list]      # 去除一个字符串首尾的所有空白，包括空格、TAB、换行符。

a_list                  # 显示 清洗后的列表a_list

b_list=[x for x in a_list if 'ea' not in x]
b_list                  # 显示 列表b_list

# 将上一步结果里的字母进行大小写转换（将大写字母转成小写，小写字母转成大写）

c_list=[x.swapcase() for x in b_list]
c_list                  # 显示 列表c_list

#将上一步结果里所有单词按 a…z 升序排列

c_list.sort()
c_list                 # 显示 排序后列表c_list
print('the list sorted:\n',c_list)      # 打印 列表排序后c_list

#最后输出结果

d_list=[x.title() for x in c_list]      # #每个单词首字母大写
r=''                # 定义一个空字符串

print(r.join(d_list))

