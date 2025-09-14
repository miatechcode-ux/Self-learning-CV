import cv2
img=cv2.imread("D:/Picture/ 2.jpg")
px=img[520,520]
print(f"此像素的BGR值为：{px}")