import cv2
import numpy as np

cap = cv2.VideoCapture("f.mp4")

if not cap.isOpened():
    raise ImportError('Cannot import file')

# table = cv2.imread('table.jpg')

key = None
while key != ord('q'):
    ret, table = cap.read()

    scale = 0.5
    table = cv2.resize(table,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('a', table)

    def draw_circle(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print x, y
            print table[y, x]

    cv2.setMouseCallback('a',draw_circle)

    lower, upper = ([30, 30, 100], [90, 90, 180])

    image = table

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    img = mask
    cv2.imshow('b', img)

    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, 10)
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.erode(img, kernel, 6)

    cv2.imshow('b1', img)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=30,param2=10,minRadius=0,maxRadius=15)

    print circles
    if circles is not None:

        height, width = img.shape
        ball = table.copy()#np.zeros((height,width,3), np.uint8)

        # circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(ball,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(ball,(i[0],i[1]),2,(0,0,255),3)


    # components = cv2.connectedComponentsWithStats(
    #     img, None, None, None, 8, cv2.CV_16U)

    # # Get info about components
    # numComponents, cmask, cstats, ccenter = components



    # for i in range(len(cstats)):
    #     cleft, ctop, cwidth, cheight, carea = cstats[i]
    #     maxsquarediff = .9
    #     if (cheight / cwidth) > maxsquarediff and (cheight / cwidth) < 1/maxsquarediff:
    #         cv2.circle(ball, (cleft, ctop), 3, (255, 0, 0))

    cv2.imshow('c', ball)

    k = cv2.waitKey(10)