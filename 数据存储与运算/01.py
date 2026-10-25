a=100
b=200
c=300
c,a,b=a,b,c

#type()函数
# print(a,b,c)
# print(type(10))
# print(type(3.1))
# print(type("jj"))
# print(type(True))
# print(type(None))

#   isinstance()函数返回bool
# num=1
# print(isinstance(num,int))

# 字符串
s1="hello"
s2='he'
s3="""#可以用'''''',但是不标准(这里成字符串的内容了）
    ss
    """#可以用'''''',但是不标准
print(s1)
print(s2)
print(s3)

s5="It 's my book"
s4='It\'s my book'#转义字符\'
print(s5)
print(s4)

m1="hello的意思是\"你好\""   #转义字符\"
m2='hello的意思是"你好"'  #也可以用单引号
print(m1)
print(m2)

print("hello\n世界")#转义字符\n换行
print("hello\t世界")#转义字符\t缩进

#---------------------------------------字符串拼接
q1="hello""world"#直接拼接
q2="人生苦短"
print(q2+"我用python")#用+号拼接

#案例------>str(int)将int类型转换成str
name="whj"
age=20
# age='20'
pro="大数据"
hobby="python"
print("大家好，我的名字是"+name+"年龄"+str(age)+"学习的专业是"+pro+"爱好是"+hobby)

#字符串格式化
#用    1.%s---占位符
print("大家好，我的名字是%s"%name)
print("大家好，我的名字是%s今年%s岁"%(name,age))
#     2.f"内容{变量/表达式}"---推荐
print(f"大家好，我的名字是{name}")
print(f"大家好，我的名字是{name}今年{age}岁")#推荐