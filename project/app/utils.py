import cv2
import numpy as np


def apply_sticker(image_data):
    image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    sticker = cv2.imread("./face.png", -1)

    if sticker is not None:
        for x, y, w, h in faces:
            sticker_resized = cv2.resize(sticker, (w, h))

            for c in range(0, 3):
                image[y : y + h, x : x + w, c] = image[y : y + h, x : x + w, c] * (
                    1 - sticker_resized[:, :, 3] / 255.0
                ) + sticker_resized[:, :, c] * (sticker_resized[:, :, 3] / 255.0)
    else:
        print("스티커 이미지를 읽어올 수 없습니다.")

    _, encoded_image = cv2.imencode(".jpeg", image)
    return encoded_image.tobytes()
