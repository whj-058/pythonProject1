#字典
#字典名称={key:value,key:value,key:value,key:value}
#----key必须为不可变类型(str,int,float,tuple)-----
#空字典-----字典名称={}或者字典名称=dict()
dict={"王林":888,"李麻花":222,"徐立国":5655}
print(dict["王林"])


#添加----字典名称[key]=value
dict["哈哈"]=222

#删除----字典名称.pop（key）或者del 字典名称[key]
a=dict.pop("哈哈")
print(a)
del dict["李麻花"]
print(dict)

#修改-----字典名称[key]=value
dict["徐立国"]=333
print(dict)

#查询-----字典名称get.[key]---根据key获取value
#---------字典名称.keys()-字典名称.values()-字典名称.items()
print(dict.values())
print(dict.items())