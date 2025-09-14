import cv2
img=cv2.imread("1231.jpg",1)
cv2.imshow("Faker",img)
retval=cv2.waitKey(0)
print(retval)
cv2.destroyAllWindows()
