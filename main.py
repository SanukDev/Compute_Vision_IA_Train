import cv2
import os

label = input("Nome do gesto (ex: OI, SIM, NAO): ")

os.makedirs(f"dataset/{label}", exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Coleta - Pressione S para salvar", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        path = f"dataset/{label}/{count}.jpg"
        cv2.imwrite(path, frame)
        print("Salvo:", path)
        count += 1

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()