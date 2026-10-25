#在一行中输入两个整数，a+b
# s=input().split()
# a=int(s[0])
# b=int(s[1])
# print(a+b)

# 一行输入两个整数a,b，空格隔开
# a, b = map(int, input().split())
# print(a + b)

# input()：读取一整行输入
# .split()：把这一行按空格切开，得到字符串列表，比如输入`3 5` → `["3","5"]`
# map(int, ...)：把列表里的两个字符串，全部转成整数
# a,b = ...：解包，分别赋值给变量`a`和`b`
# print(a+b)：计算并输出和


#输入一行两个整数c,d,计算d/c*100%，输出c,d
# c,d=map(int,input().split())
# e=(d/c)*100
# print(f"{e:.3f}"+"%")

#输入一行两个整数a，b，计算a除以b的整数商和余数，输出a除以b的商和余数，中间用空格隔开
# a,b=map(int,input().split())
# c=a//b
# d=a%b
# print(c,d)

#在一行中输入一个整数，要求a的个位数字
# a=int(input())
# c=a%10
# print(c)

##在一行中输入一个整数，要求a的十位数字
# a=int(input())
# b=abs(a)//10%10#abs()取绝对值
# print(b)

#输出一个整数，取根号后取整，输出整数
#1.n**0.5
# s=int(input())
# d=(s**0.5)//1
# print(int(d))

#2.导入math函数
# import math
# n=int(input())
# c=math.sqrt(n)
# print(int(c))

#在一行中输入一个四位整数n,输出n反向后的结果若高位为0，也需保留
# n=str(input())
# a=n[::-1]
# print(a)

#在一行中输入一个实数K,表示开尔文温度，输出实数F，C=k-237.15,F=C*1.8+32
# K=float(input())
# C=K-273.15
# F=C*1.8+32
# print(f"{F:.10f}")

#第一行输入两个整数x1，y1（表示起点的横坐标和纵坐标），第二行输入x2，y2（表示站点的横坐标和纵坐标），输出一个实数，表示两点之间的绕距(欧几里得距离公示）
# import math
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# E=(x1-x2)**2+(y1-y2)**2
# de=(math.sqrt(E))
# dm=abs(x1-x2)+abs(y1-y2)
# derta=abs(dm-de)
# print(derta)

#输入：在一行中，输入一个四位整数n
#输出：输出一个整数，表示n的各个位数之和
# n=int(input())
# x=1000<=n<=9999
# # 1. **千位**：`n // 1000` （整除 1000）
# # \(2468//1000 = 2\)
# # 2. **百位**：`(n // 100) % 10`
# # \(2468//100=24，24\%10=4\)
# # 3. **十位**：`(n // 10) % 10`
# # \(2468//10=246，246\%10=6\)
# # 4. **个位**：`n % 10`（对 10 取余）
# # \(2468\%10=8\)
# qian=n//1000
# bai=(n//100)%10
# shi=(n//10)%10
# ge=n%10
# zon=qian+bai+shi+ge
# print(zon)

#输入：在一行中输入一个整数seconds，表示要转换的秒数
#输出：在一行中输出三个整数，表示输入整数对应的小时数，分钟数，秒数（可能为0），之间用一个空格隔开
# seconds=int(input())
# shi=seconds//3600
# rem=seconds%3600
# fen=rem//60
# miao=rem%60
# print(shi ,fen ,miao)

#17输入：在一行中输入一个整数n，(1<=n<=256)表示内存大小(mb)
#输出；输出一个整数，表示在nMB内存中最多可以存储的整数个数
# n=int(input())
# if 1<=n<=256 :
#     ping=2**20
#     c=(n*ping)/4
#     print(f"{c:.0f}")

#18 给定一个长方形长a,宽b，高c，计算长方形的表面积和体积
#输入：在一行中输入三个整数a，b，c
#输出：在第一行输出一个整数，表面积S，第二行输出一个整数，体积V
#S=2(ab+bc+ca),V=abc
# a,b,c=map(int,input().split())
# S=2*(a*b+b*c+c*a)
# V=a*b*c
# print(S)
# print(V)

# 19给定作业成绩A，小测成绩B，期末成绩C，计算总成绩S
# 输入：在一行中输入三个整数A，B，C
# 输出：输出一个整数S
# S = A×20% + B×30% + C×50%
# A,B,C=map(int,input().split())
# S=A*0.2+B*0.3+C*0.5
# print(f"{S:.0f}")

#20 给定一个正整数n，计算从1到n的自然数之和
# 输入：在一行中输入一个正整数n
# 输出：输出一个整数，表示从1到n的自然数之和
# S = n*(n+1)/2
# n=int(input())
# S=n*(n+1)/2
# print(f"{S:.0f}")

#21 给定整数d（1~7代表周一到周日），推算明天是星期几
# 输入：在一行中输入一个整数d
# # 输出：输出一个整数，表示明天是星期几（范围1~7）
# d=int(input())
# if d==7:
#     print("1")
# else:
#     print(d+1)

#22 给定整数n，判断是否为闰年
# 输入：在一行中输入一个整数n
# 输出：输出字符串，闰年输出yes，否则输出no
# 闰年规则：能被400整除，或者能被4整除且不能被100整除
# n=int(input())
# if n%400==0 or (n%4==0 and n%100 !=0):
#     print("yes")
# else:
#     print("no")

#23 比较整数a和b的大小
# 输入：在一行中输入两个整数a,b
# 输出：a<b输出<；a=b输出=；a>b输出>
# a,b=map(int,input().split())
# if a<b:
#     print("<")
# elif a==b:
#     print("=")
# else:
#     print(">")

#24 卡拉兹函数，给定正整数n，计算f(n)
# 输入：在一行中输入一个正整数n
# 输出：输出一个整数，表示f(n)的值
# 规则：n为奇数，f(n)=3n+1；n为偶数，f(n)=n/2
# n=int(input())
# if n%2 !=0:
#     f=3*n+1
# else:
#     f=n/2
# print(f"{f:.0f}")

#25 牛妹数
# 描述：如果一个整数是偶数且大于 50，我们称其为牛妹数。给定一个整数 n，判断其是否为牛妹数。
# 输入：在一行中输入一个整数 n (1 ≤ n ≤ 100)。
# 输出：若 n 是牛妹数，输出 yes；否则输出 no。
# 示例1：输入50，输出no
# 示例2：输入52，输出yes
# n=int(input())
# if n%2==0 and n>50:
#     print("yes")
# else:
#     print("no")

#26 牛牛是否被叫家长
# 描述：牛牛有数学、语文、英语三门成绩，三科平均分低于60分就会被叫家长，平均分Avg=(A+B+C)/3
# 输入：在一行中输入三个整数 A,B,C (0 ≤ A,B,C ≤ 100)，用空格隔开
# 输出：如果牛牛会被叫家长，输出 YES；否则输出 NO
# 示例1：输入80 60 50，输出NO
# 示例2：输入70 55 40，输出YES
# A,B,C=map(int,input().split())
# avg=(A+B+C)/3
# if avg<60:
#     print("YES")
# else:
#     print("NO")

#27 最大最小值
# 描述：给定三个整数 a,b,c (1 ≤ a,b,c ≤ 10^6)，请输出它们中的最大值和最小值。
# 输入：在一行中输入三个整数 a,b,c，用空格隔开。
# 输出：输出两行，第一行输出'The maximum number is : X'，第二行输出'The minimum number is : Y'，冒号前后都有空格
# 示例1：输入1 2 3，输出
# The maximum number is : 3
# The minimum number is : 1
# a,b,c=map(int,input().split())
# max=max(a,b,c)
# min=min(a,b,c)
# print(f"The maximum number is : {max}")
# print(f"The minimum number is : {min}")

#28 四季
# 描述：气象意义上，3～5月为春季(spring)，6～8月为夏季(summer)，9～11月为秋季(autumn)，12月至来年2月为冬季(winter)。根据输入的年月(YYYYMM)输出对应的季节。
# 输入：在一行中输入一个六位整数YYYYMM，表示年份和月份，YYYY为四位年份，MM为两位月份(01~12)。
# 输出：输出对应的季节英文名称（全部小写）："spring"、"summer"、"autumn" 或 "winter"
# 示例1：输入201901，输出winter
# 示例2：输入202506，输出summer
# n=int(input())
# mouth=n%100
# if 3<=mouth<=5:
#     print("spring")
# elif 6<=mouth<=8:
#     print("summer")
# elif 9<=mouth<=11:
#     print("autumn")
# else:
#     print("winter")

#29 多组输入a+b II
# 描述：给定多组数据，每组两个整数a,b，计算每组数据的和
# 输入：第一行输入整数T，表示数据组数；接下来T行，每行两个整数a,b，空格隔开
# 输出：每组输出a+b的结果
# 示例：输入2，然后1 1、2 2；输出2、4
# T=int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)

#30 多组数据a+b III
# 描述：计算多组a、b的和，当a和b同时等于0的时候停止，这一组0 0不计算
# 输入：多行，每行两个整数a,b，空格隔开；0 0代表结束
# 输出：每组输出a+b的结果，一行一个
# 示例：输入1 1，2 2，0 0；输出2，4
