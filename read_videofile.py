import cv2

# read the video file
cap = cv2.VideoCapture("chaplin.mp4")

# Optional. Height and Width of the frame we will see the video output
frameWidth = 480
frameHeight = 640

# Infinite loop to read all the video frames
while True:

    # read frame by frame
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("video",img)
    # delay between each frame
    cv2.waitKey(10)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

