import numpy as np


#1.检查符合条件的元素
a=np.array([1,0,0,3,4,5,0,8])
b=np.nonzero(a)
print(b)  #不为0的下标
c=a[b]
print(c)  #输出不为0的元素 1,3,4,5,8

#2.二维数组查找
a=np.array([[1,2,0],[4,0,6],[0,8,9]])
b=np.nonzero(a)
c=a[b]
print(c)   #输出一维数组1,2,4,6,8,9

#3.查找指定条件
a=np.arange(10)
print(a)
b=np.where(a>5)
print(a[b])  #查找大于5的

#4.返回条件为true
a=np.arange(5)
b=np.array([True,False,True,True,False])
print(a[b]) #输出0,2,3
print(b[a])

#5.返回指定索引的若干个元素
a=np.array([4,3,5,7,6,8])
b=np.take(a,[0,1,4]) #返回索引为0,1,4的元素
print(b)


#5.数组排序
a=np.arange(5)
print(a[::-1])  #倒序，，-1指定步长为-1 倒数
b=np.array([3,4,1,8,4,9,5,6,9])
print(np.sort(b))  #一维数组排序

a=np.array([[3,1,5],[2,4,0]])
print(a)
b=np.sort(a,axis=0) #沿着行索引增加方向排序,也就是对每一列排序
print(b)
c=np.sort(a,axis=1) #沿着列索引增加方向排序,也就是对每一行排序
print(c)

#5.分界线排序
a=np.array([30,20,40,50,10,80,50,40,90,76])
b=np.partition(a,0)
print(b) #小于30的在左边 大于30的在右边 等于也在右边
c=np.partition(a,6)
print(c)  #小于50的在左边 大于50的在右边 等于也在右边

#6.数组统计
a=np.array([1,3,6,2,5,9,8,10,4])
print(a.max())  #最大值
print(np.max(a))  #最大值
print(np.min(a))  #最小值


a=np.arange(1,11,1).reshape(2,5) #2行5列2维数组
print(a)
print(np.max(a)) #所有元素里面的最大值
print(np.max(a,axis=0)) #行索引 找出每一列的最大值
print(np.max(a,axis=1)) #列索引 找出每一行的最大值

a=np.array([[1,3,9],[2,5,4],[6,7,8]])
print('-'*20)
print(np.max(a,axis=0)) #行索引 找出每一列的最大值
print(np.max(a,axis=1)) #列索引 找出每一行的最大值


#查找极值元素的索引
a=np.array([1,2,0,4,5,3,7,9])
print(np.argmax(a)) #索引号 7
print(np.argmin(a)) #索引号 2

a=np.array([[1,2,3],[6,5,4],[9,7,8]])  #3行3列
print(a)
print(np.argmax(a))
print(np.argmax(a,axis=0)) #每一列最大元素的索引
print(np.argmax(a,axis=1)) #每一行最大元素的索引

#计算数组平均值
a=np.arange(1,13,1).reshape(3,4)
print(a)
print(np.mean(a)) #输出 所有数的和的平均值
print(np.mean(a,axis=0)) #每一列的平均值
print(np.mean(a,axis=1)) #每一行的平均值

#计算数组加权平均值
a=np.arange(1,11)
print(a) #输出1-11的十个数
print(np.mean(a))  #没加权重
b=np.average(a,weights=np.array([1,3,1,0,0,1,1,0,1,2]))  #这是加了权重
print(b)
