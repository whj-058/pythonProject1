#不可变，不可修改，有序性，可迭代性
# s="hello-world"
# print(s[4])#o
# #切片
# print(s[0:5:1])
# print("---------------")
# print(s[-1:-7:-1])# dlrow 步长 负数从后向前

#find() 在字符串中查找字串，返回第一次出现的索引位置，找不到返回-1
s="hello-world-hello-python"
print(s.find("hello"))

#count() 统计子串在字符中出现的次数
print(s.count("hello"))

#upper() 字符串所有字符转换为大写
#lower() 字符串所有字符转换为小写
print(s.upper())#HELLO-WORLD-HELLO-PYTHON
print(s.lower()) #hello-world-hello-python

#split() 将字符串按指定分隔符分割成列表
print(s.split("-"))#['hello', 'world', 'hello', 'python']

#strip() 去除字符串两端的空白字符或指定字符
print(s.strip())

#replace() 将字符串中的指定字符替换成新的子串
print(s.replace('hello','qillo'))

#startswitch() 检查字符串是否以指定字符串开头，返回布尔值
print(s.startswith('hello'))

#案例
#用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），输出"邮箱格式正确"
emile=input("请输入你的邮箱:")
# for i in emile:
if emile.count("@")==1 and "." in emile:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")