import numpy as np

#1.数组的行拼接
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
c=np.concatenate((a,b),axis=0)  #axis=0 按行
d=np.vstack((a,b))  #行 方法
print(c)
print(d)

#2.数组的列拼接
a=np.array([[1,2],[3,4]])
b=np.array([[5],[6]])
c=np.concatenate((a,b),axis=1)  #axis=1 按列 要求具有同样的列数
d=np.hstack((a,b))  #列方法
print(c)
print(d)

#3.竖直方向将二维数组拆分成若干个数组
a=np.arange(1,21,1).reshape(4,5)
b=np.split(a,2)
c=np.vsplit(a,2)
print(b)
print(c)

#4.水平方向将二维数组拆分成若干个数组
a=np.arange(1,21,1).reshape(4,5)
b=np.hsplit(a,5)
print(b)
