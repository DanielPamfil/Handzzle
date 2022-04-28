import cv2
import HandTrackingModuleFinal as htm
import socket
import numpy


# Parameters
width, height = 1280, 720
# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detector = htm.HandDetector(maxHands=1, detectionCon=0.8)

# Cummunication
# We want to use UDP so we use DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Make sure that the address is not already used
serverAddressPort = ("127.0.0.1", 5052)

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
        # Get landmark list
        lmList = hand['lmList']
        #print(lmList)
        for lm in lmList:
            # We don't want to append directly, we need to send clean data to Unity
            # We reverse the height because on unity it is inverterd
            data.extend([lm[0], height - lm[1], lm[2]])
        #print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort)

    #img = cv2.resize(img, (0,0), None, 0.5, 0.5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)