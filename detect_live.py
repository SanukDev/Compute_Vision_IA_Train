import cv2
import numpy as np
import joblib

model = joblib.load("model.pkl")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    img = cv2.resize(frame, (64, 64))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = img.flatten().reshape(1, -1)

    prediction = model.predict(data)[0]

    cv2.putText(frame, prediction, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow("Libras IA (sem MediaPipe)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()