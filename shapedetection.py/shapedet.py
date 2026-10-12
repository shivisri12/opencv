import cv2
print("===================================================================")
print("---------------------------MAIN MENU-------------------------------")
print("===================================================================")
print("                    1. Project Details                            ")
print("                    2. Project                              ")
choice=int(input("Enter your choice:"))
print()
if choice==1:
    f=open('shapedetection.txt','r')
    s=f.read()
    print(s)
    print()
if choice==2:
    img = cv2.imread("input1.png")
    if img is None:
        print("Image not found")
        exit()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt,0.01 *cv2.arcLength(cnt,True),True)
            corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if corners == 3:
                shape = "Triangle"
            elif corners == 4:
                aspect_ratio = w / float(h)
                if 0.95 <= aspect_ratio <= 1.05:
                    shape = "Square"
                else:
                    shape = "Rectangle"
            elif corners == 5:
                shape = "Pentagon"
            elif corners == 6:
                shape = "Hexagon"
            else:
                shape="Circle"

            cv2.drawContours(img,[approx],-1,(0,0,0),3)
            cv2.putText(img,shape,(x, y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)

    cv2.imwrite("output1.png", img)
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Shape Detector", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Saved as output1.png")
    print()