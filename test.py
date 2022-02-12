import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    if ret is not None:
        cv2.imshow("camera", frame)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break
cap.release()

# Close the windows.q
cv2.destroyAllWindows()