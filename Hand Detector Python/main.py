import cv2
import HandDetector as hd
import socket
import numpy
import collections


# Parameters
width, height = 1920, 1080
# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)



# Hand Detector
detector = hd.HandDetector(maxHands=1, detectionCon=0.8)

# Cummunication
# We want to use UDP so we use DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Make sure that the address is not already used
serverAddressPort = ("127.0.0.1", 5052)

# We use a circular buffer of 5 items to mitigate the error of the click

d = collections.deque([0,0,0,1,1], maxlen=5)
while True:
    # Get the frame from the webcam
    success, img = cap.read()
    # Hands
    hands, img = detector.findHands(img)
    # Data to send to unity
    data = []
    # Landmark values - (x,y,z) * 21
    if hands:
        # Get the first hand detected
        hand = hands[0]
        # thumb(4) and index(8) coordinates
        thumb = (hand['lmList'][4][0], hand['lmList'][4][1])
        index = (hand['lmList'][8][0], hand['lmList'][8][1])
        #print(detector.fingersTouching(thumb, index))
        # Get landmark list
        lmList = hand['lmList']
        #print(lmList)
        for lm in lmList:
            # We don't want to append directly, we need to send clean data to Unity
            # We reverse the coordinates because on unity they are inverterd
            data.extend([width - lm[0], height - lm[1], lm[2]])
        # If the fingers are touching i put a 1 at the end of the stream data, 0 instead
        if detector.fingersTouching(thumb, index):
            d.append(1)
        else:
            d.append(0)
        # Add the center of the index and the thumb to the stream of data in order to use it on unity
        cx, cy = detector.fingersCenter(thumb, index)
        data.extend([width - cx, height - cy])
        # Check if at least the 70% of the last 10 contains touching fingers and in case is true sent 1 to unity
        if d.count(1) >= 3:
            data.extend([1])
        else:
            data.extend([0])

        # send the stream of data to unity
        sock.sendto(str.encode(str(data)), serverAddressPort)
        # Plot on the photo if the fingers are touching
        length, info, img = detector.findDistance(thumb, index, img)
    img = cv2.resize(img, (0,0), None, 0.5, 0.5)
    img = cv2.flip(img, 1)
    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break
