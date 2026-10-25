#函数必须先定义，在调用
#定义函数
# def out_line():
#     print("-----------------")
#     return
# out_line()

#函数的参数和返回值
#函数1：计算圆的面积
def circle_area(r):
    area=3.14*r*r
    return area
print(circle_area(10))

#函数2：计算长方形的面积
def changfang_area(l,w):
    area=l*w
    return area
a=changfang_area(10,2)
print(a)

#函数3 计算圆的面积，周长
def circle_area_len(r):
    area=round(3.14*r*r,1)#--------round(num,保留的小数位数)
    len=round(2*3.14*r,1)
    return area,len
    #return 3.14*r*r,2*3.14*r
print(circle_area_len(3))