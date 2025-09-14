import cv2

img=cv2.imread("D:/Picture/ 1.jpg")
for row in range(0,521):
    for col in range(0,521):
        img[row,col]=[255,255,255]
print(f"修改后的图片:")
cv2.imwrite("D:/Picture/3.jpg",img)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()