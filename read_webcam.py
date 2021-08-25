import cv2

# read the default webcam with id 0
cap = cv2.VideoCapture(0)

# Optional. Height and Width of the frame we will see the video output
frameWidth = 640
frameHeight = 480

# set default settings
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Infinite loop to read all the video frames
while True:

    # read frame by frame
    success, img = cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

