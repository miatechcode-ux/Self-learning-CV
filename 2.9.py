import numpy as np

n1=np.random.randint(1,3,10)
print(f"输出大小为10的范围为1到10的整数数组:")
print(f"n1={n1}")
n2=np.random.randint(5,10)
print(f"输出一个整数,且整数大于等于5小于等于10:")
print(f"n2={n2}")
n3=np.random.randint(5,size=(2,3))
print(f"输出一个2行3列的小于等于5的数组:")
print(f"n3={n3}")