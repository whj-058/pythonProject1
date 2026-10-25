#集合------>不可重复，无序，可修改
# #{}
# s1={3,45,6,2,3,4}

#定义空集合
s2=set()
#s2={}为字典

#---------------------集合常见操作--------------
# #add()---添加元素到集合中
# s1={3,45,6,2,3,4}
# s1.add(7777)
# print(s1)
#
# #remove()----移除集合中的指定元素（指定元素不存在则报错）
# s1.remove(7777)
# print(s1)
#
# #pop()----随机删除集合中的元素并返回
# s1.pop()
# print(s1)
#
# #clear()-----删除集合
# s1.clear()
# print(s1)

#difference()------两个集合的差集
#union()----------两个集合的并集
#interection()------两个集合的交集

#案例1.根据提供的班级学生的选课情况，完成如下需求：
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了法语和艺术的学生
# #方式1---intersection
# fa_set=football_set.intersection(art_set)
#方式2----& 交集
fa_set=football_set & art_set
print(fa_set)

# 2. 找出同时选修了所有四门课程的学生
all_set=football_set.intersection(basketball_set,french_set,art_set)
# all_set=football_set & basketball & french_set & art_set
print(all_set)

# 3. 找出选修了足球，但是没有选修篮球的学生
#方式1----difference
# fo_set=football_set.difference(basketball_set)
# 方式2----差集 —
# fo_set=football_set-basketball_set
#方式3----集合推导式---{要往集合添加的数据 for s in set1 if 条件}
fo_set={s for s in football_set if s not in basketball_set}
print(fo_set)


# 4. 统计每一个学生选修的课程数量
shu_set=football_set.union(basketball_set,french_set,art_set)#不可重复，下面用列表
print(shu_set)
shu_list=[*football_set,*basketball_set,*french_set,*art_set]
for i in shu_set:
    print(f"{i}选修课程次数{shu_list.count(i)}")
