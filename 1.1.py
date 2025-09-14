import cv2 # 导入视觉库
img1 = cv2.imread("123.jpg",1) # 把引号内的文件名修改为你的图片名
print("获取彩色照片的属性:")
print(f"shape:{img1.shape},size:{img1.size},type:{img1.dtype}")
img1 = cv2.imread("123.jpg",0)
print("获取灰色照片的属性:")
print(f"shape:{img1.shape},size:{img1.size},type:{img1.dtype}")