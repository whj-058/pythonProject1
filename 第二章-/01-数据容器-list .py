#定义列表
# s=["a","b","c","d","e"]
#
# #切片操作 s[开始索引:结束索引:步长]
# print(s[0:3:1])
# print(s[:3:1])
# print(s[:3])#a,b,c
# print(s[:-2])#a,b,c
# print(s[3])#d
#
# #append() 尾部追加元素
# s.append("f")
# print(s)
#
# #insert() 在指定索引之前，插入该元素
# s.insert(0,1)
# print(s)
#
# #remove() 移除第一个匹配的值
# s.remove("a")
# print(s)
#
# #pop() 删除列表中指定索引的元素，未指定则最后一个
# s.pop(1)
# print(s)
#
# #sort() 对列表进行排序
# y=[2,3,65,1,4,23]
# y.sort()
# print(y)
#
# #reverse() 反转列表元素
# y.reverse()
# print(y)


#案例1 将用户输入的10个数字存储到列表中，并将列表中的数字进行排序，最大值，最小值，平均值
# s=[]
# for i in range(10):
#     num=int(input("请输入一个有效的数字"))
#     s.append(num)
# s.sort()
# print("最小值：",s[0])
# print("最大值：",s[-1])
# print("平均值：",sum(s)/len(s))

#案例2 合并两个列表中的元素，并对合并的结果进行去重处理
# num_list1=[19,23,54,64,875,20,109,232,123,12]
# num_list2=[55,80,72,35,60,123,54,23,78]
# # num_list=num_list1+num_list2#1.直接用加号
# num_list=[*num_list1,*num_list2]#2.进行解包
# print(f"合并后的列表是:{num_list}")
#
# new_list=[]
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(f"去重后的列表：{new_list}")