import os
import cv2

from app.basegui import BaseGUIWindow as bgw

class Camera:
    FRAME_WIDTH = 1280
    FRAME_HEIGHT = 720

    def __init__(self):
        self.camera_ok()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.FRAME_HEIGHT)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cap.release()

    def camera_ok(self):
        """method to check for camera presence. On posix systems"""
        if os.path.exists('/dev/video0'):
            return True
        else:
            raise RuntimeError("Camera not installed")
        
    def feed(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Problem reading from camera")
        return frame

    @staticmethod
    def feed_to_bytes(img):
        new_image_size = tuple(int(x * 0.6) for x in bgw.SCREEN_SIZE)
        return cv2.imencode(
            ".png",
            cv2.resize(
                img,
                dsize=new_image_size,
                fx=0.6,
                fy=0.6,
                interpolation=cv2.INTER_AREA,
            ),
        )[1].tobytes()