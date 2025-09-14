import numpy as np
list=[1,2,3]
n1=np.array(list,float)
n2=[1,2,3]
nd=np.array(n2,ndmin=3)
print(f"n1={n1},n1的数据类型:{n1.dtype},{type(n1[0])},nd={nd}")