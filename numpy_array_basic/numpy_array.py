import numpy as np
import matplotlib.pyplot as plt

print(np.zeros(10))  #一维全零数组
print(np.zeros((3,3),dtype=np.int))  #多维tupple数组  3行3列  可以加数据类型
print(np.ones(10))   #一维全1数组
print(np.ones((4,4)))   #多维全1数组
print(np.full((3,5),8))  #可以指定数组元素的值
print(np.identity(4))   #创建单位矩阵
print(np.eye(4,4,1))    #4行4列单位矩阵 对角线从下标1开始


print(np.array([1,23,4,'ltf','fjf']))   #可以随便传入数据  一维数组
print(np.array([[1,2,3],['ltf','lsq','fjf'],['男','女','人妖']]))   #多维数组，随便定义、

a=np.array([[1,2,3],[4,3,6]])
b=np.full_like(a,3.2)
c=np.ones_like(a)
print(b)
print(c)

#根据一个向量创建斜对角线方阵 也可以指定对角线位置
arr2d=np.diag([1,2,3,4])
print(arr2d)

print(np.arange(1,6))  #类似于range 不包含上界
print(np.arange(1,10,2))   #开始 结束 步长
print(np.linspace(1,10,4))  #开始 结束 个数
print(np.logspace(1,4,4))     #分为4个等分点，形成数组【1,2,3,4】然后形成 对数的底数的指数
print(np.logspace(1,5,5,base=2))  #指定对数为2


#创建坐标系 其实可以用plt.show()
x=np.linspace(0,1,5)
y=np.linspace(0,1,3)
xv,yv=np.meshgrid(x,y)
print(xv)
print(yv)
plt.plot(xv,yv,'^')
plt.show()


#指数图
x=np.arange(-5,5,0.1)
y=np.power(2,x)
#print(y)
plt.plot(x,y)
#对数图
x=np.power(2,x)
y=np.log2(x)
plt.plot(x,y)
plt.show()


x1=np.arange(1,5,1)
y1=np.power(x1,3)  #x1的3次方
print(y1)

x2=np.array([1,8,27,64])
y2=np.power(x2,1/3)  #x2的1/3次方
print(y2)
