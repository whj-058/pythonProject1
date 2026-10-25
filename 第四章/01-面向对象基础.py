class Car():
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        print("Car类的对象初始化完毕")

     # 定义实例方法
    def running(self):
        print(f"{self.brand},{self.name}汽车正在高速运行中")

    def total_cost(self,discount,rate):
        '''
        计算提车费用，
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        '''
        total_cost=self.price*discount+rate*self.price
        return total_cost
    #定义魔法方法
    def __str__(self):
        return f"{self.brand},{self.name},{self.price},{self.color}"
    def __eq__(self, other):
        return self.color==other.color and self.brand==other.brand and self.price==other.price and self.name==other.name
    def __lt__(self, other):
        return self.price<other.price
c1=Car("红色","奔驰","a1",1000000)
c2=Car("白色","宝马","a2",8222200)
print(c1.__dict__)
c1.running()
total=c1.total_cost(0.9,0.1)
print(total)
print(c1)
print(c2)
print(c1==c2)
print(c1<c2)


