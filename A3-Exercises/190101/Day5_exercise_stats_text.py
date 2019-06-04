#1、创建 Day5_exercise_stats_text.py 文件
#2、使用字典（dict）统计字符样本text中各个英文单词出现的次数
#3、示例：{'is': 10, 'better': 9, …}
#4、按照出现的次数从大到小输出所有的单词及出现的次数
#5、只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等

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

from operator import itemgetter, attrgetter

a=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
a=a.lower()               # 将所有英文字符改为小写
b_list=a.split()           # 以空格拆分独立的单词，返回列表
c=set(b_list)                # 创建集合，自动去重 

d={x:a.count(x) for x in c}     #创建字典

d                   # 显示字典

result=sorted(d.items(), key=itemgetter(1), reverse=True)  



for k  in result:      # 打印字典
    print(k)    


