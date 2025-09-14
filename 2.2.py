import cv2
img=cv2.imread("D:/Picture/ 1.jpg")
px=img[520,520]
print(f"此位置的像素值为{px}")
px=[255,255,255]
print(f"修改后的此位置的像素值为{px}")