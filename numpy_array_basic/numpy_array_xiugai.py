import numpy as np


#1.访问二维数组
a=np.arange(1,16,1).reshape(3,5) #3行5列数组
print(a)
print(a[1])  #访问第一行
print(a[1,1])  #访问第一行第一列的元素
print(a[1][1])  #访问第一行第一列的元素

#2.访问二维数组部分元素
print('-'*20)
b=np.arange(1,16,1).reshape(3,5) #3行5列二维数组
print(b)
print(b[0:1,2:4]) #第一行下标为2和下标为3的元素
print(b[:,3])     #所有行下标为3的列数的所有元素
print(b[:,2:5])   #所有行，2,3,4列元素


#3.删除元素
print('-'*20)
c=np.arange(1,16,1).reshape(3,5) #3行5列二维数组
print(c)
print(np.delete(c,1))  #删除行号 返回一位数组
print(np.delete(c,[2,3,8,9]))  #返回一位数组 删除下标为2,3,8,9的元素

#4.删除列元素
print('-'*20)
d=np.arange(1,16,1).reshape(3,5) #3行5列二维数组
print(d)
print(np.delete(d,1,axis=0))  #删除下标为1这一行
print(np.delete(d,[2,3],axis=1))  #删除下标为2和3 的这两列


#5.插入元素
print('-'*20)
e=np.array([[1,2],[3,4],[5,6]])
print(e)
print(np.insert(e,1,5)) #返回一维数组 把5插入到1号索引后
print(np.insert(e,1,5,axis=1))  #插入一列 该列元素全为5
print(np.insert(e,1,[0,2,5],axis=1)) #插入一列 为0,2,5
print(np.insert(e,len(e),[[7,8]],axis=0))  #在最后一列插入一行
print(np.c_[e,np.array([1,1,1])]) #在最后一行后面加一列
print(np.append(e,[[7,8]],axis=0))  #append追加一列


