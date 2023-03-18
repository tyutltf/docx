import numpy as np


#1  赋值 改变原数组
a=np.array([1,2,3,4,5])
b=a
b[0]=100
print(b)
print(a)

#2 拷贝 不改变原数组
a1=np.array([1,2,3,4,5])
b1=np.copy(a1)
b1[0]=20
print(a1)
print(b1)

#3  修改
arry=np.array([1,2,3,4,5])
#arry[2]=10
arry[0:2]=8  #包头不包尾
print(arry)

arr1=np.array([[1,2,3,4],[5,6,7,8]])
print(arr1.T)  #数组的转置
arr1.shape=4,2
print(arr1)    #简单分隔

#4 分隔
arr2=np.arange(0,20,1)
print(arr2.reshape(4,5))
newarr2=arr2.reshape(4,5)
newarr2[0:2,0]=8  #0行1行 的0列 为8
print(newarr2)

#5
newarr3=np.reshape(newarr2,(1,-1))  #行数为1,  列数 待定
print(newarr3)
newarr4=np.reshape(newarr2,(-1,1))  #列数为1， 行数 待定
print(newarr4)

newarr5=newarr3[0][:,np.newaxis]   #取第一行 即一维数组 在变成一列
print(newarr5)


#6 二维数组转一维数组
arr2d=np.arange(1,21,1).reshape(4,5) #4行5列
print(arr2d)
arr2d1=np.ravel(arr2d)
print(arr2d1)  #arr2d1和arr2d共享同一块内存
print(arr2d.flatten())   #不共享内存

#7 resize使用
arrresize=np.resize(arr2d,(5,2))  #5行2列  本来有20个元素 只取其中的10个也可以 不像reshape必须全取
print(arrresize)

#8 转置  多维转换置换 
arr3d=np.arange(1,28,1).reshape(3,3,3)
print(arr3d)
arr3d1=np.transpose(arr3d)
print(arr3d1)
