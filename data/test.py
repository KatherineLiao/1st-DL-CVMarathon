import cv2

img_path = 'data/lena.png'

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
print(img)


#b g r 分別在img的通道順序是 0,1,2

#只取 Blue 通道
b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

#只取 Green 通道
g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

#只取 Green 通道
r = img.copy()
# set blue and red channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0


# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    # 顯示彩圖
    
    cv2.imshow("bgr", img)
    # 顯示三個通道
    cv2.imshow("B_Channel", b)
    cv2.imshow("G_Channel", g)
    cv2.imshow("R_Channel", r)

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break