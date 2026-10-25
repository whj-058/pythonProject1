#输入与输出
#input（）
#print()

#案例-------银行取款
#1.输入密码
total=10000
password=input("请输入密码")
print("密码正确")
#2.输入取款金额
num=input("请输入取款金额:")
#3.计算并输出
print(f"你的余额为{total-int(num)}")